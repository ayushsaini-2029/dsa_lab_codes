public class FirstLabQuestion2 {

	public static int linearSearch(int[] array, int target) {
		for (int index = 0; index < array.length; index++) {
			if (array[index] == target) {
				return index;
			}
		}
		return -1;
	}

	public static int binarySearch(int[] array, int target) {
		int low = 0;
		int high = array.length - 1;

		while (low <= high) {
			int middle = low + (high - low) / 2;
			if (array[middle] == target) {
				return middle;
			}
			if (array[middle] < target) {
				low = middle + 1;
			} else {
				high = middle - 1;
			}
		}
		return -1;
	}

	public static void main(String[] args) {
		int[] arraySizes = {10_000, 50_000, 100_000};
		final int warmupIterations = 100;
		final int measuredIterations = 1_000;

		System.out.println("Binary Search vs Linear Search");
		System.out.println("Target is the last element in each sorted array.");
		System.out.println("Array Size\tTarget Index\tLinear (microseconds)\tBinary (microseconds)");

		for (int size : arraySizes) {
			int[] array = new int[size];
			for (int index = 0; index < size; index++) {
				array[index] = index;
			}

			int target = array[size - 1];
			for (int iteration = 0; iteration < warmupIterations; iteration++) {
				linearSearch(array, target);
				binarySearch(array, target);
			}

			int linearChecksum = 0;
			long linearStart = System.nanoTime();
			for (int iteration = 0; iteration < measuredIterations; iteration++) {
				linearChecksum += linearSearch(array, target);
			}
			long linearElapsed = System.nanoTime() - linearStart;

			int binaryChecksum = 0;
			long binaryStart = System.nanoTime();
			for (int iteration = 0; iteration < measuredIterations; iteration++) {
				binaryChecksum += binarySearch(array, target);
			}
			long binaryElapsed = System.nanoTime() - binaryStart;

			double linearAverage = (double) linearElapsed / measuredIterations / 1_000;
			double binaryAverage = (double) binaryElapsed / measuredIterations / 1_000;
			int targetIndex = linearChecksum / measuredIterations;
			if (targetIndex != binaryChecksum / measuredIterations) {
				throw new IllegalStateException("Search methods returned different indexes.");
			}

			System.out.printf("%d\t\t%d\t\t%.3f\t\t\t%.3f%n",
					size, targetIndex, linearAverage, binaryAverage);
		}
	}
}
