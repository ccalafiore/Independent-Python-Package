
import math
import typing


__all__ = ["FloatRange"]


class FloatRange:

    @typing.overload
    def __init__(self, stop: float | int, /) -> None: ...

    @typing.overload
    def __init__(self, start: float | int, stop: float | int, step: float | int = 1, /) -> None: ...

    def __init__(self, *args):

        n = len(args)

        if n == 1:
            start, stop, step = 0, args[0], 1

        elif n > 1:
            start, stop = args[0], args[1]
            assert isinstance(start, (float, int))

            if n == 2:
                step = 1
            elif n == 3:
                step = args[2]
                assert isinstance(step, (float, int))
                assert step != 0, 'step argument must not be zero'
            else:
                raise TypeError(f'FloatRange expected at most 3 arguments, got {n}')
        else:
            raise TypeError(f'FloatRange expected at least 1 arguments, got {n}')

        assert isinstance(stop, (float, int))

        self.start = start
        self.stop = stop
        self.step = step
        self._is_ascend = self.step > 0

    def __iter__(self):

        self._i = self.start
        self._is_first = True
        return self

    def __next__(self):

        if self._is_first:
            self._is_first = False
        else:
            self._i += self.step

        if self._is_ascend:
            is_iter_not_done = self._i < self.stop
        else:
            is_iter_not_done = self._i > self.stop

        if is_iter_not_done:
            return self._i
        else:
            raise StopIteration


    def __len__(self):

        if self._is_ascend:
            is_not_zero = self.start < self.stop
        else:
            is_not_zero = self.start > self.stop

        if is_not_zero:
            return math.ceil((self.stop - self.start) / self.step)
        else:
            return 0

    def __str__(self):

        return type(self).__name__ + f'(start={self.start}, stop={self.stop}, step={self.step}, len={len(self)})'
