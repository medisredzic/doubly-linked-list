from typing import Union

from My_ListNode import My_ListNode


class My_DoublyLinkedList:
    """A base class providing a doubly linked list representation."""

    ## Do not change! ##

    def __init__(self, new_head: Union[None, 'My_ListNode'] = None, new_tail: Union[None, 'My_ListNode'] = None,
                 new_size=0):
        """Create a list and default values are None."""
        self._header = new_head
        self._tail = new_tail
        self._size = new_size
        self._descending = True

    def _len_(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    def descending(self) -> bool:
        """Return the current order type of the list."""
        return self._descending

    def list_is_empty(self) -> bool:
        """Return True if list is empty."""
        return self._size == 0

    def _get_header(self) -> Union[None, 'My_ListNode']:
        return self._header

    def _get_tail(self) -> Union[None, 'My_ListNode']:
        return self._tail

    # EXAMPLE 2
    # The following methods are required for example 2.

    def _insert(self, character_val: str) -> None:
        """Add the element `character_val` to the list, keeping the list in descending/ascending order, depending on
        the descending property.

        Args:
            character_val (str): Character value to be added.

        Raises:
            ValueError: If character_val is not an integer.
        """
        """if isinstance(character_val, int):
            return ValueError"""

        new_node = My_ListNode(character_val)
        tmp = self._header
        tmp2 = None

        if self._header is None:
            self._header = new_node
            self._tail = new_node
            self._tail.set_next_node(None)
            new_node.set_prev_node(None)
            new_node.set_next_node(None)
            self._size += 1
            return

        if self.descending():
            if self._header.get_data() <= new_node.get_data():
                self._header.set_prev_node(new_node)
                self._header = new_node
                new_node.set_next_node(tmp)
                self._size += 1
                return
            else:
                while tmp is not None:
                    if tmp.get_data() <= new_node.get_data():
                        new_node.set_next_node(tmp)
                        new_node.set_prev_node(tmp.get_prev_node())
                        tmp.get_prev_node().set_next_node(new_node)
                        tmp.set_next_node(tmp.get_next_node())
                        tmp.set_prev_node(new_node)
                        self._size += 1
                        return
                    if tmp.get_next_node() is not None:
                        tmp2 = tmp
                    tmp = tmp.get_next_node()
                else:
                    tmp2.get_next_node().set_next_node(new_node)
                    self._tail = new_node
                    self._tail.set_prev_node(tmp2.get_next_node())
                    self._tail.set_next_node(None)
                    self._size += 1
        else:
            if self._header.get_data() >= new_node.get_data():
                self._header.set_prev_node(new_node)
                self._header = new_node
                new_node.set_next_node(tmp)
                self._size += 1
                return
            else:
                while tmp is not None:
                    if tmp.get_data() >= new_node.get_data():
                        new_node.set_next_node(tmp)
                        new_node.set_prev_node(tmp.get_prev_node())
                        tmp.get_prev_node().set_next_node(new_node)
                        tmp.set_next_node(tmp.get_next_node())
                        tmp.set_prev_node(new_node)
                        self._size += 1
                        return
                    if tmp.get_next_node() is not None:
                        tmp2 = tmp
                    tmp = tmp.get_next_node()
                else:
                    tmp2.get_next_node().set_next_node(new_node)
                    self._tail = new_node
                    self._tail.set_prev_node(tmp2.get_next_node())
                    self._tail.set_next_node(None)
                    self._size += 1
        return

    def get_character_value(self, index: int) -> str:
        """Return the value (data) at position `index`, without removing the node.

        Args:
            index (int): 0 <= index < Length of list

        Returns:
            (String): Retrieved value.

        Raises:
            ValueError: If the passed index is not an integer or out of range.
        """
        if not isinstance(index, int):
            raise ValueError

        cur = self._header
        counter = 0
        while cur is not None:
            if counter == index:
                return cur.get_data()
            else:
                counter += 1
                cur = cur.get_next_node()

        return ValueError

    def _remove(self, character_val: str) -> bool:
        """Remove the first occurence of given character value `character_val`.

        Args:
            character_val (str): the value to remove

        Returns:
            (bool): Whether an element was successully removed or not.

        Raises:
            ValueError: If the passed character is not a string
       """
        if self._size == 0:
            return False

        if character_val is None:
            raise ValueError

        cur_node = self._header

        if self._header.get_data() == character_val:
            if self._header.get_next_node() is not None:
                self._header.get_next_node().set_prev_node(None)
            else:
                self._tail = None
            self._header = self._header.get_next_node()
            self._size -= 1
            return True

        elif self._tail.get_data() == character_val:
            self._tail = self._tail.get_prev_node()
            self._tail.set_next_node(None)
            self._size -= 1
            return True

        while cur_node is not None:
            if cur_node.get_data() == character_val:
                if cur_node.get_prev_node() is not None:
                    cur_node.get_prev_node().set_next_node(cur_node.get_next_node())
                    cur_node.get_next_node().set_prev_node(cur_node.get_prev_node())
                    self._size -= 1
                    return True
                else:
                    self._header = cur_node.get_next_node()
                    cur_node.get_next_node().set_prev_node(None)
                    self._size -= 1

            cur_node = cur_node.get_next_node()
        return False

    def _remove_all(self, character_val: str) -> bool:
        """Remove every character value `character_val` in the list.

        Args:
            character_val (str): the value to remove

        Returns:
            (bool): Whether an element was successully removed or not.

        Raises:
            ValueError: If the passed character is not a string
       """
        if not isinstance(character_val, str):
            return ValueError

        count = 0
        cur_node = self._header
        while cur_node is not None:
            if cur_node.get_data() == character_val:
                self._remove(character_val)
                count += 1

            cur_node = cur_node.get_next_node()

        if count == 0:
            return False
        else:
            return True

    def remove_duplicates(self) -> None:
        """Remove all duplicates from the list such that the remaining elements are all unique.

        Example:
            ['a','a','d','d','d','f','g'] -> ['a','d','f','g']
        """
        cur_node = self._header
        lst = []
        while cur_node is not None:
            if cur_node.get_data() not in lst:
                lst.append(cur_node.get_data())
            else:
                self._remove(cur_node.get_data())

            cur_node = cur_node.get_next_node()

    def reorder_list(self):
        """Reorder list from a descending order into an ascending order and vice versa. It also changes the way how
        the list inserts future elements to the list (in descending order, when it was changed to descending order and
        vice versa). No return value nor an error is specified, as this method is an internal method
        
        Example: ['a','d','f','g'] -> ['g','f','d','a'] -> ['a','d','f','g'].
        """

        return
