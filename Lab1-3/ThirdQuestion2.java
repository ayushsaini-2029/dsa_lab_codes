import java.util.Scanner;

public class ThirdQuestion2 {

	private static class Node {
		private int data;
		private Node previous;
		private Node next;

		private Node(int data) {
			this.data = data;
		}
	}

	private Node head;
	private Node tail;

	public void insertAtHead(int data) {
		Node newNode = new Node(data);
		newNode.next = head;

		if (head == null) {
			tail = newNode;
		} else {
			head.previous = newNode;
		}

		head = newNode;
	}

	public void insertAtTail(int data) {
		Node newNode = new Node(data);
		newNode.previous = tail;

		if (tail == null) {
			head = newNode;
		} else {
			tail.next = newNode;
		}

		tail = newNode;
	}

	public boolean deleteByValue(int value) {
		Node current = head;
		while (current != null && current.data != value) {
			current = current.next;
		}

		if (current == null) {
			return false;
		}

		if (current.previous == null) {
			head = current.next;
		} else {
			current.previous.next = current.next;
		}

		if (current.next == null) {
			tail = current.previous;
		} else {
			current.next.previous = current.previous;
		}

		return true;
	}

	public void displayForward() {
		if (head == null) {
			System.out.println("List is empty.");
			return;
		}

		Node current = head;
		while (current != null) {
			System.out.print(current.data + " <-> ");
			current = current.next;
		}
		System.out.println("NULL");
	}

	public void displayReverse() {
		if (tail == null) {
			System.out.println("List is empty.");
			return;
		}

		Node current = tail;
		while (current != null) {
			System.out.print(current.data + " <-> ");
			current = current.previous;
		}
		System.out.println("NULL");
	}

	private static void printMenu() {
		System.out.println("\n1. Insert at head");
		System.out.println("2. Insert at tail");
		System.out.println("3. Delete by value");
		System.out.println("4. Display forward");
		System.out.println("5. Display in reverse");
		System.out.println("6. Exit");
		System.out.print("Choose an action: ");
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		ThirdQuestion2 list = new ThirdQuestion2();
		int choice;

		do {
			printMenu();
			choice = scanner.nextInt();

			switch (choice) {
				case 1:
					System.out.print("Enter data: ");
					list.insertAtHead(scanner.nextInt());
					System.out.println("Node inserted at head.");
					break;
				case 2:
					System.out.print("Enter data: ");
					list.insertAtTail(scanner.nextInt());
					System.out.println("Node inserted at tail.");
					break;
				case 3:
					System.out.print("Enter value to delete: ");
					if (list.deleteByValue(scanner.nextInt())) {
						System.out.println("First matching node deleted.");
					} else {
						System.out.println("Value not found.");
					}
					break;
				case 4:
					list.displayForward();
					break;
				case 5:
					list.displayReverse();
					break;
				case 6:
					System.out.println("Exiting doubly linked-list program.");
					break;
				default:
					System.out.println("Invalid choice. Select an option from 1 to 6.");
			}
		} while (choice != 6);

		scanner.close();
	}
}
