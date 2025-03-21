import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ShellCommandExecutor {

    public static void main(String[] args) {
            String reportFormat = "csv,html"; // Example input
                    executeReportCommand(reportFormat);
                        }

                            public static void executeReportCommand(String reportFormat) {
                                    // Split the reportFormat string into individual formats
                                            String[] formats = reportFormat.split(",");

                                                    // Base command components
                                                            String command = "axe";
                                                                    String subCommand = "reporter";
                                                                            String inputDir = "./axe-reports/json/";
                                                                                    String outputDir = "./axe-reports/";

                                                                                            // Initialize the command list with base components
                                                                                                    List<String> commandList = new ArrayList<>();
                                                                                                            commandList.add(command);
                                                                                                                    commandList.add(subCommand);
                                                                                                                            commandList.add(inputDir);
                                                                                                                                    commandList.add(outputDir);

                                                                                                                                            // Add format arguments
                                                                                                                                                    for (String format : formats) {
                                                                                                                                                                commandList.add("--format=" + format);
                                                                                                                                                                        }

                                                                                                                                                                                // Create a ProcessBuilder with the command list
                                                                                                                                                                                        ProcessBuilder processBuilder = new ProcessBuilder(commandList);

                                                                                                                                                                                                try {
                                                                                                                                                                                                            // Start the process
                                                                                                                                                                                                                        Process process = processBuilder.start();

                                                                                                                                                                                                                                    // Wait for the process to complete
                                                                                                                                                                                                                                                int exitCode = process.waitFor();
                                                                                                                                                                                                                                                            System.out.println("Command executed with exit code: " + exitCode);
                                                                                                                                                                                                                                                                    } catch (IOException | InterruptedException e) {
                                                                                                                                                                                                                                                                                e.printStackTrace();
                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                            