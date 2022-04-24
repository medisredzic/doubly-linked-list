from typing import Union

class My_ListNode:

    def __init__(self, data: str, prev_node=None, next_node=None):
        self._data = data
        self._next_node = next_node
        self._prev_node = prev_node

    def get_data(self) -> int:
        return self._data

    def set_data(self, new_data: str) -> int:
        self._data = new_data

    def get_next_node(self) -> Union[None, 'My_ListNode']:
        return self._next_node

    def get_prev_node(self) -> Union[None, 'My_ListNode']:
        return self._prev_node

    def set_next_node(self, _node: Union[None, 'My_ListNode']) -> None:
        self._next_node = _node

    def set_prev_node(self, _node: Union[None, 'My_ListNode']) -> None:
        self._prev_node = _node
