import unittest
from datetime import date

from My_DoublyLinkedList import My_DoublyLinkedList
from My_ListNode import My_ListNode

list = None
TestListHead = None
TestListTail = None

arrListDefault = ['z', 'y', 'x', 'u', 'd', 'c', 'b', 'a']
arrListShort = ['z', 'y', 'c', 'b', 'a']
arrListWithDuplicates = ['z', 'z', 'x', 'u', 'u', 'u', 'b', 'b']
arrListWithoutDuplicates = ['z', 'x', 'u', 'b']

arrListReorder1   		= ['z', 'y', 'c', 'b', 'a']
arrListReorder1Result 	= ['a', 'b', 'c', 'y', 'z']
arrListReorder1Element  = ['a']

maxPoints = 14.0        # defines the maximum achievable points for the example tested here
points = maxPoints      # stores the actually achieved points based on failed unit tests

class UnitTestTemplate(unittest.TestCase):
    strTutor          = ""
    strAssignment     = "Assignment03-Example01"
    strHorLine        = "------------------------------------------------------------\n"
    strFileHeader     = "ALGORITHMS AND DATA STRUCTURES 1 AI - " +strAssignment+"\n"+"("+str(date.today())+")\n"+strHorLine+"\n"

    strCorrection = []

    def setUp(self):
        pass

    def tearDown(self):
       pass

    ####################################################
    # Definition of test cases
    ####################################################

    def createListFromArray(self,arrList=[]):
        # reset head and tail
        global TestListTail
        global TestListHead

        if (len(arrList) > 0):
            # store first element and update head and tail
            TestListHead =  My_ListNode(arrList[0])
            TestListTail = TestListHead

            for i in range(1,len(arrList)):
                temp_node = My_ListNode(arrList[i])
                # if i ==1:
                #     TestListHead.set_next_node()
                temp_node.set_prev_node(TestListTail)
                TestListTail.set_next_node(temp_node)
                TestListTail = temp_node
            return True
        else:
            return False

    def testListForward(self, head=None, tail=None, list=[]):
        current = head

        if (len(list) == 0):
            if(head == None and tail == None):
                return None
            else:
                return "List should be empty - head or tail is not None!"

        elif(len(list) == 1):
            if (head != tail):
                return "Head and tail are not equal in a list with size 1!"
            if (head.get_next_node() != None):
                return "Next of Head/Tail should be None (listsize == 1)!"
            if (head.get_prev_node() != None):
                return "Prev of Head/Tail should be None (listsize == 1)!"
            if (list[0] != head.get_data()):
                return "Wrong element at index 0 (head)! Expected ["+str(list[0])+"] but found ["+str(head.get_data())+"]"
            else:
                return None
        # list with size > 1
        for i in range(0,len(list)):
            if(current == head):
                if(current.get_next_node() == None):
                    return "Next of head is None (listsize > 1)!"
                if(list[i] != current.get_data()):
                    return "Wrong element at index "+str(i)+" (head)! Expected ["+str(list[i])+"] but found ["+str(current.get_data())+"]"
                if(list[i+1] != current.get_next_node().get_data()):
                    return "Wrong next element of index "+str(i)+" (head)! Expected ["+str(list[i+1])+"] but found ["+str(current.get_next_node().get_data())+"]"

            elif(current == tail):
                if(list[i] != current.get_data()):
                    return "Wrong element at index "+str(i)+" (tail)! Expected ["+str(list[i])+"] but found ["+str(current.get_data())+"]"
                if(current.get_next_node() != None):
                    return "Next of tail is not None!"

            else:
                if(list[i] != current.get_data()):
                    return "Wrong element at index "+str(i)+"! Expected ["+str(list[i])+"] but found ["+str(current.get_data())+"]"
                if current.get_next_node() == None:
                    return "Wrong next element of index "+str(i)+"! Expected ["+str(list[i+1])+"] but found None"
                elif (list[i + 1] != current.get_next_node().get_data()):
                    return "Wrong next element of index " + str(i) + "! Expected [" + str(
                        list[i + 1]) + "] but found [" + str(current.get_next_node().get_data()) + "]"

            current=current.get_next_node()

        return None

    def testListBackward(self, head=None, tail=None, list=[]):
        current = tail

        if (len(list) == 0):
            if(head == None and tail == None):
                return None
            else:
                return "List should be empty - head or tail is not None!"

        elif(len(list) == 1):
            if (head != tail):
                return "Head and tail are not equal in a list with size 1!"
            if (tail.get_prev_node() != None):
                return "Prev of Head/Tail should be None (listsize == 1)!"
            if (tail.get_next_node() != None):
                return "NExt of Head/Tail should be None (listsize == 1)!"
            if (list[len(list)-1] != tail.get_data()):
                return "Wrong element at index 0 (head)! Expected ["+str(list[len(list)-1])+"] but found ["+str(tail.get_data())+"]"
            else:
                return None
        # list with size > 1
        for i in range((len(list)-1),-1,-1):

            if(current == head):
                if(current.get_prev_node() != None):
                    return "Prev of head is not None (listsize > 1)!"
                if(list[i] != current.get_data()):
                    return "Wrong element at index "+str(i)+" (head)! Expected ["+str(list[i])+"] but found ["+str(current.get_data())+"]"

            elif(current == tail):
                if(list[i] != current.get_data()):
                    return "Wrong element at index "+str(i)+" (tail)! Expected ["+str(list[i])+"] but found ["+str(current.get_data())+"]"
                if(current.get_prev_node() == None):
                    return "Prev of tail is None!"

            else:
                if(list[i] != current.get_data()):
                    return "Wrong element at index "+str(i)+"! Expected ["+str(list[i])+"] but found ["+str(current.get_data())+"]"
                if current.get_prev_node() == None:
                    return "Wrong next element of index "+str(i)+"! Expected ["+str(list[i-1])+"] but found None"
                elif (list[i-1] != current.get_prev_node().get_data()):
                    return "Wrong prev element of index "+str(i)+"! Expected ["+str(list[i-1])+"] but found ["+str(current.get_prev_node().get_data())+"]"



            current = current.get_prev_node()

        return None

    # def testTemp(self):
    # 	list = My_LinkedList()
    #
    # 	list.insert_ordered(3)
    # 	self.assertEqual("<custom arrListReorderOnlyOddElementserror description>\n    ",2, list.get(0))

    def test_RemoveDuplicates(self):

        self.createListFromArray(arrListWithDuplicates)
        list = My_DoublyLinkedList(TestListHead, TestListTail, len(arrListWithDuplicates))
        result = None
        #print("test_RemoveDuplicates ", list._get_header())
        result = self.testListForward(list._get_header(), list._get_tail(), arrListWithDuplicates)
        self.assertIsNone(result)
        result = self.testListBackward(list._get_header(), list._get_tail(), arrListWithDuplicates)
        self.assertIsNone(result)

        # /*System.out.print("\nList before removing duplicates: ");
        # for(Object elem : convertListtoArray(list._get_header(), list._len_())) {
        # 	System.out.print((Integer)elem+" ");
        # }*/
        list.remove_duplicates()
        # /*System.out.print("\nList after removing duplicates:  ");
        # for(Object elem : convertListtoArray(list._get_header(), list._len_())) {
        # 	System.out.print((Integer)elem+" ");
        # }*/

        result = self.testListForward(list._get_header(), list._get_tail(), arrListWithoutDuplicates)
        # print(list._get_header().get_data(), list._get_tail().get_data(), arrListWithoutDuplicates)
        self.assertIsNone(result, "Remove duplicates - testing list forward:"+str(result))
        result = self.testListBackward(list._get_header(), list._get_tail(), arrListWithoutDuplicates)
        self.assertIsNone(result, "Remove duplicates - testing list backward:"+str(result))

    def test_SizeWithInsertOnly(self):
        list = My_DoublyLinkedList()

        self.assertTrue(list.list_is_empty(), "Empty list must have size 0!\n -->")

        list._insert('a')
        self.assertEqual(1, list._len_(), "List after inserting one element must have size 1!\n -->")
        list._insert('b')
        self.assertEqual(2, list._len_(), "List after inserting two elements must have size 2!\n -->")
        list._insert('c')
        self.assertEqual(3, list._len_(), "List after inserting three elements must have size 3!\n -->")
        list._insert('d')
        self.assertEqual(4, list._len_(), "List after inserting four elements must have size 4!\n -->")

    def test_SizeWithInsertAndRemove(self):
        list = My_DoublyLinkedList()
        self.assertTrue(list.list_is_empty(), "Empty list must have size 0!\n -->")

        list._insert('a')
        self.assertEqual(1, list._len_(), "List after inserting one element must have size 1!\n -->")
        list._insert('b')
        self.assertEqual(2, list._len_(), "List after inserting one element must have size 2!\n -->")
        list._insert('c')
        self.assertEqual(3, list._len_(), "List after inserting one element must have size 3!\n -->")
        list._insert('d')
        self.assertEqual(4, list._len_(), "List after inserting one element must have size 4!\n -->")

        list._remove('a')
        self.assertEqual(3, list._len_(), "After removing one element of a list with 4 elements must have size 3!\n -->")
        list._remove('b')
        self.assertEqual(2, list._len_(), "After removing one element of a list with 3 elements must have size 3!\n -->")
        list._remove('c')
        self.assertEqual(1, list._len_(), "After removing one element of a list with 2 elements must have size 3!\n -->")
        list._remove('d')
        self.assertEqual(0, list._len_(), "After removing one element of a list with 1 elements must have size 3!\n -->")

    def test_InsertSorted(self):
        result = ""
        list = My_DoublyLinkedList()

        # at beginning (empty list) head/tail must be None
        self.assertIsNone(list._get_header(),"In an empty list head must point to None!\n -->")
        self.assertIsNone(list._get_tail(),"In an empty list tail must point to None!\n -->")

        list._insert('b')
        self.assertIsNone(list._get_header().get_prev_node(), "After inserting one element head->prev must point to None!\n -->")
        self.assertIsNone(list._get_tail().get_next_node(), "After inserting one element tail->next must point to None!\\n -->")

        list._insert('y')
        result = self.testListForward(list._get_header(), list._get_tail(), ['y','b'])
        self.assertIsNone(result, "After inserting e.g. [y][b]: "+str(result)+"\n -->")
        # print("Header ",list._header.get_data())
        # print("Tail ",list._tail.get_data())
        result = self.testListBackward(list._get_header(), list._get_tail(), ['y','b'])
        self.assertIsNone(result, "After inserting e.g. [y][b]: "+str(result)+"\n -->")

        list._insert('c')
        result = self.testListForward(list._get_header(), list._get_tail(), ['y','c','b'])
        self.assertIsNone(result, "After inserting e.g. [y][c][b]: "+str(result)+"\n -->")
        result = self.testListBackward(list._get_header(), list._get_tail(), ['y','c','b'])
        self.assertIsNone(result, "After inserting e.g. [y][c][b]: "+str(result)+"\n -->")

        list._insert('a')
        result = self.testListForward(list._get_header(), list._get_tail(), ['y','c','b','a'])
        self.assertIsNone(result, "After inserting e.g. [y][c][b][a]: "+str(result)+"\n -->")
        result = self.testListBackward(list._get_header(), list._get_tail(), ['y','c','b','a'])
        self.assertIsNone(result, "After inserting e.g. [y][c][b][a]: "+str(result)+"\n -->")

        list._insert('z')
        result = self.testListForward(list._get_header(), list._get_tail(), ['z','y','c','b','a'])
        self.assertIsNone(result, "After inserting e.g. [z][y][c][b][a]: "+str(result)+"\n -->")
        result = self.testListBackward(list._get_header(), list._get_tail(), ['z','y','c','b','a'])
        self.assertIsNone(result, "After inserting e.g. [z][y][c][b][a]: "+str(result)+"\n -->")

    def test_InsertSortedWithNullObject(self):
        list = My_DoublyLinkedList()

        # insertion of None object is not allowed
        try:
            list._insert(None)
        except Exception as e:
            self.assertTrue(e.__class__ == ValueError, "Null objects must not be inserted into list!\n -->")

    def test_Clear(self):

        my_test_list=My_DoublyLinkedList()

        assert my_test_list._get_header() is None
        assert my_test_list._get_tail() is None
        assert my_test_list._len_() == 0

        my_test_list._insert(2)
        my_test_list._insert(3)
        my_test_list._insert(1)

        my_test_list=My_DoublyLinkedList()

        self.assertEqual(0, my_test_list._len_(),
                         "Method 'clear()': After clearing the list _len_() should return 0!\n -->")
        self.assertIsNone(my_test_list._get_header(),
                          "Method 'clear()': After clearing the list head should point to None!\n -->")
        self.assertIsNone(my_test_list._get_tail(),
                          "Method 'clear()': After clearing the list tail should point to None!\n -->")

    def test_InsertSorted3EqualKeys(self):
        list = My_DoublyLinkedList()

        list._insert(2)
        self.assertEqual(2, list._get_header().get_data(), "Method 'insert_ordered()': After inserting one a valid element the head element is not correct!\n -->")
        self.assertEqual(2, list._get_tail().get_data(), "Method 'insert_ordered()': After inserting one a valid element the tail element is not correct!\n -->")
        self.assertTrue(list._get_header() == list._get_tail(), "Method 'insert_ordered()': After inserting one a valid element the head and tail reference must point to the same element!\n -->")

        list._insert(2)
        self.assertEqual(2, list._get_header().get_data(), "Method 'insert_ordered()': After inserting two equal and valid elements the head element is not correct!\n -->")
        self.assertEqual(2, list._get_tail().get_data(), "Method 'insert_ordered()': After inserting two equal and valid elements the tail element is not correct!\n -->")
        self.assertFalse(list._get_header() == list._get_tail(), "Method 'insert_ordered()': After inserting two equal and valid elements the head and tail reference must not have the same reference!\n -->")

    def test_ReorderList(self):
        global TestListTail
        global TestListHead
        self.createListFromArray(arrListReorder1)
        list = My_DoublyLinkedList(TestListHead, TestListTail, len(arrListReorder1))

        result = self.testListForward(list._get_header(), list._get_tail(), arrListReorder1)

        self.assertIsNone(result, "ERROR in replacing testlist!!!")
        result = self.testListBackward(list._get_header(), list._get_tail(), arrListReorder1)
        self.assertIsNone(result, "ERROR in replacing testlist!!!")

        list.reorder_list()

        self.assertEqual('a', list.get_character_value(0),
                         "Method 'reorder_list()': Returned index of first element is incorrect; was " + list.get_character_value(0) + " but needs to be " + 'a' + "\n-->")

    def test_ReorderListWith1Element(self):
        global TestListTail
        global TestListHead
        self.createListFromArray(arrListReorder1Element)
        list = My_DoublyLinkedList(TestListHead, TestListTail, len(arrListReorder1Element))
        result = None

        result = self.testListForward(list._get_header(), list._get_tail(), arrListReorder1Element)
        self.assertIsNone(result, "ERROR in replacing testlist!!!\n -->")
        result = self.testListBackward(list._get_header(), list._get_tail(), arrListReorder1Element)
        self.assertIsNone(result, "ERROR in replacing testlist!!!\n -->")

        list.reorder_list()
        #self.assertEqual(-1, idx,
        #                 "Method 'reorder_list()': Returned index of first element is incorrect; was " + str(
        #                     idx) + " but needs to be " + str(1) + "\n-->")

        result = self.testListForward(list._get_header(), list._get_tail(), arrListReorder1Element)
        self.assertIsNone(result, "Method 'reorder_list()' on list with 1 element: "+str(result)+"\n -->")
        result = self.testListBackward(list._get_header(), list._get_tail(), arrListReorder1Element)
        self.assertIsNone(result, "Method 'reorder_list()' on list with 1 element: "+str(result)+"\n -->")

    def test_Get(self):
        global TestListTail
        global TestListHead
        reason = "Method 'get()': Wrong element returned!\n -->"
        self.createListFromArray(arrListDefault)	# ['z', 'y', 'x', 'u', 'd', 'c', 'b', 'a']
        list = My_DoublyLinkedList(TestListHead, TestListTail, len(arrListDefault))
        print(list._header, list._tail, list._size)
        # print(type(list._get_header().get_next_node()))
        self.assertEqual('z', list.get_character_value(0), reason)
        self.assertEqual('y', list.get_character_value(1), reason)
        self.assertEqual('x', list.get_character_value(2), reason)
        self.assertEqual('u', list.get_character_value(3), reason)
        self.assertEqual('d', list.get_character_value(4), reason)
        self.assertEqual('c', list.get_character_value(5), reason)
        self.assertEqual('b', list.get_character_value(6), reason)
        self.assertEqual('a', list.get_character_value(7), reason)

        try:
            list.get_character_value(21)
        except Exception as e:
            # print(e.__class__ == ValueError)
            self.assertTrue(e.__class__ == ValueError, "Method 'get': Accessing a position out of bounds should throw an ValueError!\n -->")
        try:
            list.get_character_value(-1)
        except Exception as e:
            self.assertTrue(e.__class__ == ValueError, "Method 'get': Accessing a position out of bounds (e.g. -1) should throw an ValueError!\n -->")

    def test_RemoveOnEmptyList(self):
        list = My_DoublyLinkedList()
        self.assertFalse(list._remove('a'), "Method '_remove()': Removing an element from an empty list should return false!\n -->")


    def test_RemoveNullObject(self):
        global TestListTail
        global TestListHead
        reason = "method '_remove()': If parameter None is passed an ValueError should be thrown!\n -->"
        self.createListFromArray(arrListShort)	#{1,4,6,7,10}
        list = My_DoublyLinkedList(TestListHead, TestListTail, len(arrListShort))
        try:
            list._remove(0)
        except Exception as e:
            self.assertTrue(e.__class__ == ValueError, reason)

    def test_Remove(self):
        result = None
        global TestListTail
        global TestListHead
        reason = "Method '_remove()': Element couldn't be removed correctly!\n -->"
        self.createListFromArray(arrListShort)	#{1,4,6,7,10} ['z', 'y', 'c', 'b', 'a']
        list = My_DoublyLinkedList(TestListHead, TestListTail, len(arrListShort))

        result = self.testListForward(list._get_header(), list._get_tail(), arrListShort)
        self.assertIsNone(result, "ERROR in replacing testlist!!!\n -->")
        result = self.testListBackward(list._get_header(), list._get_tail(), arrListShort)
        self.assertIsNone(result, "ERROR in replacing testlist!!!\n -->")

        self.assertTrue(list._remove('z'), reason)
        result = self.testListForward(list._get_header(), list._get_tail(),['y','c', 'b', 'a'])
        self.assertIsNone(result, reason)
        result = self.testListBackward(list._get_header(), list._get_tail(),['y','c', 'b', 'a'])
        self.assertIsNone(result, reason)


        self.assertTrue(list._remove('a'), reason)
        result = self.testListForward(list._get_header(), list._get_tail(),['y','c','b'])
        self.assertIsNone(result, reason)
        result = self.testListBackward(list._get_header(), list._get_tail(),['y','c','b'])
        self.assertIsNone(result, reason)

        self.assertTrue(list._remove('c'), reason)
        result = self.testListForward(list._get_header(), list._get_tail(),['y','b'])
        self.assertIsNone(result, reason)
        result = self.testListBackward(list._get_header(), list._get_tail(),['y','b'])
        self.assertIsNone(result, reason)

        self.assertTrue(list._remove('y'), reason)
        result = self.testListForward(list._get_header(), list._get_tail(),['b'])
        self.assertIsNone(result, reason)
        result = self.testListBackward(list._get_header(), list._get_tail(),['b'])
        self.assertIsNone(result, reason)


        self.assertFalse(list._remove('s'), "Method '_remove()': Removing an element which is not in the list should return false!\n -->")


        self.assertTrue(list._remove('b'), reason)
        self.assertIsNone(list._get_header(), "Method '_remove()': After removing all elements from list head reference should be None!\n -->")
        self.assertIsNone(list._get_tail(), "Method '_remove()': After removing all elements from list tail reference should be None!\n -->")
        self.assertEqual(0, list._len_(), "Method '_remove()': After removing all elements from list the list size should be 0!\n -->")

    def test_GetFromEmptyList(self):
        list = My_DoublyLinkedList()
        self.assertIsNone(list._get_header(), "Method 'get()': In a new MyLinkedList() the head reference should be null!\n -->")
        self.assertIsNone(list._get_tail(), "Method 'get()': In a new MyLinkedList() the tail reference should be null!\n -->")
        self.assertEqual(0, list._len_(), "Method 'get()': In a new MyLinkedList() the size should be 0!\n -->")

        try:
            list.get_character_value(0)
        except Exception as e:
            self.assertTrue(e.__class__ ==  ValueError, "Method 'get()': The attempt of getting any element from an empty list should throw an ValueError!\n -->")

    def convertListtoArray(self, head, size):
        arr = [None] * size
        i = 0

        current = head
        while (current != None):
            arr[i] = current.get_data()
            i+=1
            current = current.get_next_node()

        return arr