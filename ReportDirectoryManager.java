import java.io.IOException;
import java.nio.file.*;
import java.util.stream.Stream;

public class ReportDirectoryManager {

    // Static flag to track directory initialization
    private static boolean isReportDirectoryInitialized = false;

    // Synchronized method to ensure thread safety
    public static synchronized void initializeReportDirectory() {
        // Check if the directory has already been initialized
        if (!isReportDirectoryInitialized) {
            Path reportDirectoryPath = Paths.get("report");
            try {
                // Check if the directory exists
                if (Files.exists(reportDirectoryPath)) {
                    // If the directory exists, delete its contents
                    try (Stream<Path> files = Files.list(reportDirectoryPath)) {
                        files.forEach(file -> {
                            try {
                                Files.deleteIfExists(file);
                            } catch (IOException e) {
                                System.err.println("Failed to delete file: " + file + " - " + e.getMessage());
                            }
                        });
                    }
                    System.out.println("Report directory contents cleared.");
                } else {
                    // If the directory does not exist, create it
                    Files.createDirectory(reportDirectoryPath);
                    System.out.println("Report directory created.");
                }
                // Set the flag to true after initialization
                isReportDirectoryInitialized = true;
            } catch (IOException e) {
                // Handle potential IO exceptions
                System.err.println("An error occurred while initializing the report directory: " + e.getMessage());
            }
        }
    }



}

