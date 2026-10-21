public class FirstLabQuestion1 {
    

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

	public static long quadraticOperation(int[] array) {
		long total = 0;
		for (int outerIndex = 0; outerIndex < array.length; outerIndex++) {
			for (int innerIndex = 0; innerIndex < array.length; innerIndex++) {
				total += array[outerIndex] * array[innerIndex];
			}
		}
		return total;
	}

	public static void main(String[] args) {
        System.out.println("Question 1//");

		int[] arraySizes = {10_000, 50_000, 100_000};
		final int warmupIterations = 100;
		final int measuredIterations = 1_000;

		System.out.println("Linear Search Execution Time");
		System.out.println("Array Size\tTarget Index\tAverage Time (microseconds)");

		for (int size : arraySizes) {
			int[] array = new int[size];
			for (int index = 0; index < size; index++) {
				array[index] = index;
			}

			int target = array[size - 1];
			for (int iteration = 0; iteration < warmupIterations; iteration++) {
				linearSearch(array, target);
			}

			int checksum = 0;
			long startTime = System.nanoTime();
			for (int iteration = 0; iteration < measuredIterations; iteration++) {
				checksum += linearSearch(array, target);
			}
			long elapsedNanos = System.nanoTime() - startTime;
			double averageMicroseconds = (double) elapsedNanos / measuredIterations / 1_000;

			int targetIndex = checksum / measuredIterations;
			System.out.printf("%d\t\t%d\t\t%.3f%n", size, targetIndex, averageMicroseconds);

            
		}
	}
}