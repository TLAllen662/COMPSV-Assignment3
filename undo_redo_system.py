"""Design Memo

A stack is the right choice for undo and redo because editing history is naturally
last in, first out (LIFO). The most recent action is the first action a user
expects to reverse. When an action is undone, it moves from the undo stack to
the redo stack. Redoing it reverses that transfer. This arrangement keeps both
histories ordered and makes each operation a constant-time pointer update.
Starting a new action after an undo clears the redo stack because that previous
future history no longer belongs to the current timeline.

A queue is better suited for a help desk because customers should be served in
the order they arrive: first in, first out (FIFO). Enqueue adds a ticket at the
rear, while dequeue removes the ticket at the front. The front and rear
pointers let the system serve customers fairly without moving every remaining
customer after each service.

These implementations differ from Python's built-in lists because they use
explicit Node objects and next pointers rather than a contiguous, indexable
array. The stack tracks only its top node, and the queue tracks both its front
and rear nodes. Push, pop, enqueue, and dequeue therefore update links instead
of shifting or resizing list elements. Lists provide convenient indexing,
slicing, and many built-in operations, while these structures expose only the
operations appropriate to their abstract data types. The linked approach also
demonstrates the underlying pointer relationships directly, although it does
not provide constant-time random access like a list does.
"""

from undo_redo import Stack

def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack
            undo_stack.push(action)
            redo_stack = Stack()


            print(f"Action performed: {action}")
        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            action = undo_stack.pop()
            if action is not None:
                redo_stack.push(action)
                print(f"Undid action: {action}")
            else:
                print("No actions to undo")

        elif choice == "3":
            # Pop an action from the redo stack and push it onto the undo stack
            action = redo_stack.pop()
            if action is not None:
                undo_stack.push(action)
                print(f"Redid action: {action}")
            else:
                print("No actions to redo")


        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.print_stack()

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.print_stack()

        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()