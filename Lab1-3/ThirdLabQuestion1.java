import java.util.Scanner;

public class ThirdLabQuestion1 {

	private static class Node {
        private int data;
		private Node next;

		private Node(int data) {
			this.data = data;
		}
	}

	private Node head;
	private int size;

	public void insertAtHead(int data) {
        System.out.println("Question 1//");
		Node newNode = new Node(data);
		newNode.next = head;
		head = newNode;
		size++;
	}

	public void insertAtTail(int data) {
		Node newNode = new Node(data);
		if (head == null) {
			head = newNode;
		} else {
			Node current = head;
			while (current.next != null) {
				current = current.next;
			}
			current.next = newNode;
		}
		size++;
	}

	public boolean insertAtIndex(int data, int index) {
		if (index < 0 || index > size) {
			return false;
		}
		if (index == 0) {
			insertAtHead(data);
			return true;
		}
		if (index == size) {
			insertAtTail(data);
			return true;
		}

		Node previous = nodeAt(index - 1);
		Node newNode = new Node(data);
		newNode.next = previous.next;
		previous.next = newNode;
		size++;
		return true;
	}

	public boolean deleteByKey(int target) {
		if (head == null) {
			return false;
		}
		if (head.data == target) {
			head = head.next;
			size--;
			return true;
		}

		Node previous = head;
		while (previous.next != null && previous.next.data != target) {
			previous = previous.next;
		}
		if (previous.next == null) {
			return false;
		}

		previous.next = previous.next.next;
		size--;
		return true;
	}

	private Node nodeAt(int index) {
		Node current = head;
		for (int currentIndex = 0; currentIndex < index; currentIndex++) {
			current = current.next;
		}
		return current;
	}

	public void traverse() {
		if (head == null) {
			System.out.println("List is empty.");
			return;
		}

		Node current = head;
		while (current != null) {
			System.out.print(current.data + " -> ");
			current = current.next;
		}
		System.out.println("NULL");
	}

	private static void printMenu() {
		System.out.println("\n1. Insert at head");
		System.out.println("2. Insert at tail");
		System.out.println("3. Insert at index");
		System.out.println("4. Delete by matching data key");
		System.out.println("5. Traverse list");
		System.out.println("6. Exit");
		System.out.print("Choose an action: ");
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		ThirdLabQuestion1 list = new ThirdLabQuestion1();
		int choice;

		do {
			printMenu();
			choice = scanner.nextInt();

			switch (choice) {
				case 1: {
					System.out.print("Enter data: ");
					int data = scanner.nextInt();
					list.insertAtHead(data);
					System.out.println("Node inserted at head.");
					break;
				}
				case 2: {
					System.out.print("Enter data: ");
					int data = scanner.nextInt();
					list.insertAtTail(data);
					System.out.println("Node inserted at tail.");
					break;
				}
				case 3: {
					System.out.print("Enter data: ");
					int data = scanner.nextInt();
					System.out.print("Enter index (0 to " + list.size + "): ");
					int index = scanner.nextInt();
					if (list.insertAtIndex(data, index)) {
						System.out.println("Node inserted at index " + index + ".");
					} else {
						System.out.println("Insertion failed: invalid index.");
					}
					break;
				}
				case 4: {
					System.out.print("Enter data key to delete: ");
					int target = scanner.nextInt();
					if (list.deleteByKey(target)) {
						System.out.println("First matching node deleted.");
					} else {
						System.out.println("No matching node found.");
					}
					break;
				}
				case 5:
					list.traverse();
					break;
				case 6:
					System.out.println("Exiting linked-list program.");
					break;
				default:
					System.out.println("Invalid choice. Select an option from 1 to 6.");
			}
		} while (choice != 6);

		scanner.close();
	}
}
