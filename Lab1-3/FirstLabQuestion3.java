public class FirstLabQuestion3 {

	public static long nestedLoopOperation(int size) {
		long total = 0;
		for (int outerIndex = 0; outerIndex < size; outerIndex++) {
			for (int innerIndex = 0; innerIndex < size; innerIndex++) {
				total += (long) (outerIndex + 1) * (innerIndex + 1);
			}
		}
		return total;
	}

	public static void main(String[] args) {
		int[] dataSizes = {500, 1_000, 2_000, 4_000};
		final int warmupIterations = 3;
		final int measuredIterations = 5;

		System.out.println("Nested Loop Performance (O(n^2))");
		System.out.println("Each run performs size * size matrix-style operations.");
		System.out.println("Data Size\tOperations\tAverage Time (milliseconds)\tResult Check");

		for (int size : dataSizes) {
			for (int iteration = 0; iteration < warmupIterations; iteration++) {
				nestedLoopOperation(size);
			}

			long checksum = 0;
			long startTime = System.nanoTime();
			for (int iteration = 0; iteration < measuredIterations; iteration++) {
				checksum += nestedLoopOperation(size);
			}
			long elapsedNanos = System.nanoTime() - startTime;

			double averageMilliseconds = (double) elapsedNanos / measuredIterations / 1_000_000;
			long expectedResult = (long) size * size * (size + 1) * (size + 1) / 4;
			String resultCheck = checksum / measuredIterations == expectedResult ? "PASS" : "FAIL";

			System.out.printf("%d\t\t%d\t\t%.3f\t\t\t%s%n",
					size, (long) size * size, averageMilliseconds, resultCheck);
		}
	}
}

