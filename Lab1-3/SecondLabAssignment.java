import java.util.Scanner;

public class SecondLabAssignment {

	private static final int INSERT = 1;
	private static final int DELETE = 2;
	private static final int SEARCH = 3;
	private static final int DISPLAY = 4;
	private static final int EXIT = 5;

	public static void insert(int[] array, int[] size, int index, int value) {
		for (int currentIndex = size[0]; currentIndex > index; currentIndex--) {
			array[currentIndex] = array[currentIndex - 1];
		}
		array[index] = value;
		size[0]++;
	}

	public static int delete(int[] array, int[] size, int index) {
		int deletedValue = array[index];
		for (int currentIndex = index; currentIndex < size[0] - 1; currentIndex++) {
			array[currentIndex] = array[currentIndex + 1];
		}
		size[0]--;
		return deletedValue;
	}

	public static int search(int[] array, int size, int target) {
		for (int index = 0; index < size; index++) {
			if (array[index] == target) {
				return index;
			}
		}
		return -1;
	}

	private static void display(int[] array, int size) {
		System.out.print("Database: [");
		for (int index = 0; index < size; index++) {
			if (index > 0) {
				System.out.print(", ");
			}
			System.out.print(array[index]);
		}
		System.out.println("]");
	}

	private static void printMenu() {
		System.out.println("\n1. Insert element");
		System.out.println("2. Delete element");
		System.out.println("3. Search for value");
		System.out.println("4. Display database");
		System.out.println("5. Exit");
		System.out.print("Choose an action: ");
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		System.out.print("Enter database capacity: ");
		int capacity = scanner.nextInt();
		while (capacity <= 0) {
			System.out.print("Capacity must be positive. Enter capacity again: ");
			capacity = scanner.nextInt();
		}

		int[] database = new int[capacity];
		int[] size = {0};

		System.out.print("Enter initial number of elements (0 to " + capacity + "): ");
		int initialSize = scanner.nextInt();
		while (initialSize < 0 || initialSize > capacity) {
			System.out.print("Enter a valid initial size: ");
			initialSize = scanner.nextInt();
		}

		for (int index = 0; index < initialSize; index++) {
			System.out.print("Enter element at index " + index + ": ");
			database[index] = scanner.nextInt();
		}
		size[0] = initialSize;

		int choice;
		do {
			printMenu();
			choice = scanner.nextInt();

			switch (choice) {
				case INSERT:
					if (size[0] == capacity) {
						System.out.println("Insertion failed: database is full.");
						break;
					}
					System.out.print("Enter value to insert: ");
					int value = scanner.nextInt();
					System.out.print("Enter index (0 to " + size[0] + "): ");
					int insertIndex = scanner.nextInt();
					if (insertIndex < 0 || insertIndex > size[0]) {
						System.out.println("Insertion failed: invalid index.");
					} else {
						insert(database, size, insertIndex, value);
						System.out.println("Element inserted successfully.");
						display(database, size[0]);
					}
					break;
				case DELETE:
					if (size[0] == 0) {
						System.out.println("Deletion failed: database is empty.");
						break;
					}
					System.out.print("Enter index to delete (0 to " + (size[0] - 1) + "): ");
					int deleteIndex = scanner.nextInt();
					if (deleteIndex < 0 || deleteIndex >= size[0]) {
						System.out.println("Deletion failed: invalid index.");
					} else {
						int deletedValue = delete(database, size, deleteIndex);
						System.out.println("Deleted element: " + deletedValue);
						display(database, size[0]);
					}
					break;
				case SEARCH:
					System.out.print("Enter value to search for: ");
					int target = scanner.nextInt();
					int foundIndex = search(database, size[0], target);
					if (foundIndex == -1) {
						System.out.println("Value not found.");
					} else {
						System.out.println("First match found at index: " + foundIndex);
					}
					break;
				case DISPLAY:
					display(database, size[0]);
					break;
				case EXIT:
					System.out.println("Exiting database program.");
					break;
				default:
					System.out.println("Invalid choice. Select an option from 1 to 5.");
			}
		} while (choice != EXIT);

		scanner.close();
	}
}
