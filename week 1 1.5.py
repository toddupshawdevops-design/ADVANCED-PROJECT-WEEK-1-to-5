/*
 * ============================================================
 * PROJECT WEEK 1
 * Inheritance, Composition, and User Interactions
 *
 * Name: Todd Upshaw
 * Date: August 11, 2026
 *
 * Purpose:
 * This Java application demonstrates inheritance, composition,
 * object instantiation, and basic user interaction through a
 * console-based IT Asset Management System.
 * ============================================================
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


/*
 * ============================================================
 * BASE CLASS / MAIN APPLICATION
 * ============================================================
 *
 * Asset is the base class.
 *
 * This class also contains the main() method so the program
 * can be executed directly as Asset.java.
 */
public class Asset {

    private String assetId;
    private String description;
    private String assignedTo;

    /*
     * Constructor for Asset.
     */
    public Asset(
            String assetId,
            String description,
            String assignedTo) {

        this.assetId = assetId;
        this.description = description;
        this.assignedTo = assignedTo;
    }

    /*
     * Getters.
     */
    public String getAssetId() {
        return assetId;
    }

    public String getDescription() {
        return description;
    }

    public String getAssignedTo() {
        return assignedTo;
    }

    /*
     * Setter.
     */
    public void setAssignedTo(String assignedTo) {
        this.assignedTo = assignedTo;
    }

    /*
     * Returns the type of asset.
     */
    public String getAssetType() {
        return "General Asset";
    }

    /*
     * Formats asset information for display.
     */
    public String displayInfo() {

        return String.format(
                "%-10s %-12s %-25s %-20s",
                assetId,
                getAssetType(),
                description,
                assignedTo
        );
    }


    /*
     * ========================================================
     * MAIN METHOD
     * ========================================================
     */
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        /*
         * COMPOSITION:
         *
         * The AssetInventory object manages a collection
         * of Asset objects.
         */
        AssetInventory inventory = new AssetInventory();

        /*
         * Load realistic sample data.
         */
        inventory.addAsset(
                new Laptop(
                        "LAP-1001",
                        "Dell Latitude 5540",
                        "Sarah Johnson",
                        "Windows 11 Pro"
                )
        );

        inventory.addAsset(
                new Laptop(
                        "LAP-1002",
                        "Lenovo ThinkPad T14",
                        "Michael Carter",
                        "Windows 11 Pro"
                )
        );

        inventory.addAsset(
                new Server(
                        "SRV-2001",
                        "Application Server",
                        "DevOps Team",
                        "Production"
                )
        );


        /*
         * ====================================================
         * WELCOME SCREEN
         * ====================================================
         */

        System.out.println();
        System.out.println(
                "=============================================================="
        );

        System.out.println(
                "                       PROJECT WEEK 1"
        );

        System.out.println(
                "        INHERITANCE, COMPOSITION, AND USER INTERACTIONS"
        );

        System.out.println();

        System.out.println(
                "                IT ASSET MANAGEMENT SYSTEM"
        );

        System.out.println();

        System.out.println(
                "                       Todd Upshaw"
        );

        System.out.println(
                "=============================================================="
        );

        System.out.println();

        System.out.println(
                "Welcome to the IT Asset Management System!"
        );

        System.out.println();

        System.out.println(
                "This application allows you to manage IT assets."
        );

        System.out.println(
                "You can display, add, update, or delete assets."
        );

        System.out.println();

        System.out.println(
                "The application demonstrates:"
        );

        System.out.println(
                "  - Inheritance"
        );

        System.out.println(
                "  - Composition"
        );

        System.out.println(
                "  - Object-oriented programming"
        );

        System.out.println(
                "  - User input and output"
        );

        System.out.println(
                "=============================================================="
        );


        /*
         * ====================================================
         * MAIN MENU LOOP
         * ====================================================
         */

        boolean running = true;

        while (running) {

            System.out.println();
            System.out.println(
                    "----------------------- MAIN MENU ----------------------------"
            );

            System.out.println("1. Display all assets");
            System.out.println("2. Add laptop");
            System.out.println("3. Add server");
            System.out.println("4. Update asset assignment");
            System.out.println("5. Delete asset");
            System.out.println("6. Exit");

            System.out.println(
                    "--------------------------------------------------------------"
            );

            System.out.print(
                    "Enter your selection: "
            );

            String choice = scanner.nextLine();


            /*
             * Process the user's selection.
             */
            switch (choice) {

                case "1":

                    inventory.displayAllAssets();

                    break;


                case "2":

                    System.out.println();
                    System.out.println(
                            "----------------------- ADD LAPTOP ---------------------------"
                    );

                    System.out.print(
                            "Enter Asset ID: "
                    );

                    String laptopId = scanner.nextLine();

                    System.out.print(
                            "Enter laptop description: "
                    );

                    String laptopDescription =
                            scanner.nextLine();

                    System.out.print(
                            "Enter assigned employee/team: "
                    );

                    String laptopAssignedTo =
                            scanner.nextLine();

                    System.out.print(
                            "Enter operating system: "
                    );

                    String operatingSystem =
                            scanner.nextLine();


                    /*
                     * INHERITANCE:
                     *
                     * Laptop inherits from Asset.
                     */
                    Laptop laptop = new Laptop(
                            laptopId,
                            laptopDescription,
                            laptopAssignedTo,
                            operatingSystem
                    );


                    /*
                     * COMPOSITION:
                     *
                     * Add the Laptop object to AssetInventory.
                     */
                    inventory.addAsset(laptop);

                    System.out.println(
                            "Laptop added successfully."
                    );

                    break;


                case "3":

                    System.out.println();
                    System.out.println(
                            "----------------------- ADD SERVER ---------------------------"
                    );

                    System.out.print(
                            "Enter Asset ID: "
                    );

                    String serverId = scanner.nextLine();

                    System.out.print(
                            "Enter server description: "
                    );

                    String serverDescription =
                            scanner.nextLine();

                    System.out.print(
                            "Enter assigned employee/team: "
                    );

                    String serverAssignedTo =
                            scanner.nextLine();

                    System.out.print(
                            "Enter server environment: "
                    );

                    String environment =
                            scanner.nextLine();


                    /*
                     * INHERITANCE:
                     *
                     * Server inherits from Asset.
                     */
                    Server server = new Server(
                            serverId,
                            serverDescription,
                            serverAssignedTo,
                            environment
                    );


                    /*
                     * COMPOSITION:
                     *
                     * Add Server to AssetInventory.
                     */
                    inventory.addAsset(server);

                    System.out.println(
                            "Server added successfully."
                    );

                    break;


                case "4":

                    System.out.println();
                    System.out.println(
                            "--------------------- UPDATE ASSET --------------------------"
                    );

                    System.out.print(
                            "Enter Asset ID: "
                    );

                    String updateId =
                            scanner.nextLine();

                    System.out.print(
                            "Enter new employee/team assignment: "
                    );

                    String newAssignee =
                            scanner.nextLine();

                    inventory.updateAssignment(
                            updateId,
                            newAssignee
                    );

                    break;


                case "5":

                    System.out.println();
                    System.out.println(
                            "--------------------- DELETE ASSET --------------------------"
                    );

                    System.out.print(
                            "Enter Asset ID to delete: "
                    );

                    String deleteId =
                            scanner.nextLine();

                    inventory.deleteAsset(deleteId);

                    break;


                case "6":

                    running = false;

                    System.out.println();
                    System.out.println(
                            "=============================================================="
                    );

                    System.out.println(
                            "Thank you for using the IT Asset Management System."
                    );

                    System.out.println(
                            "Goodbye, Todd!"
                    );

                    System.out.println(
                            "=============================================================="
                    );

                    break;


                default:

                    System.out.println();

                    System.out.println(
                            "Invalid selection."
                    );

                    System.out.println(
                            "Please enter a number from 1 through 6."
                    );
            }
        }

        scanner.close();
    }
}


/*
 * ============================================================
 * CHILD CLASS - LAPTOP
 * ============================================================
 *
 * INHERITANCE:
 *
 * Laptop extends Asset.
 */
class Laptop extends Asset {

    private String operatingSystem;


    public Laptop(
            String assetId,
            String description,
            String assignedTo,
            String operatingSystem) {

        super(
                assetId,
                description,
                assignedTo
        );

        this.operatingSystem =
                operatingSystem;
    }


    /*
     * INHERITANCE:
     *
     * Override getAssetType().
     */
    @Override
    public String getAssetType() {

        return "Laptop";
    }


    /*
     * Override displayInfo().
     */
    @Override
    public String displayInfo() {

        return String.format(
                "%-10s %-12s %-25s %-20s OS: %s",
                getAssetId(),
                getAssetType(),
                getDescription(),
                getAssignedTo(),
                operatingSystem
        );
    }
}


/*
 * ============================================================
 * CHILD CLASS - SERVER
 * ============================================================
 *
 * INHERITANCE:
 *
 * Server extends Asset.
 */
class Server extends Asset {

    private String environment;


    public Server(
            String assetId,
            String description,
            String assignedTo,
            String environment) {

        super(
                assetId,
                description,
                assignedTo
        );

        this.environment =
                environment;
    }


    /*
     * INHERITANCE:
     *
     * Override getAssetType().
     */
    @Override
    public String getAssetType() {

        return "Server";
    }


    /*
     * Override displayInfo().
     */
    @Override
    public String displayInfo() {

        return String.format(
                "%-10s %-12s %-25s %-20s Environment: %s",
                getAssetId(),
                getAssetType(),
                getDescription(),
                getAssignedTo(),
                environment
        );
    }
}


/*
 * ============================================================
 * COMPOSITION CLASS
 * ============================================================
 *
 * AssetInventory demonstrates COMPOSITION.
 *
 * It contains a collection of Asset objects.
 */
class AssetInventory {

    /*
     * COMPOSITION:
     *
     * AssetInventory owns a collection of Asset objects.
     *
     * final prevents the reference from being reassigned.
     * Assets can still be added and removed from the list.
     */
    private final List<Asset> assets;


    public AssetInventory() {

        assets = new ArrayList<>();
    }


    /*
     * Add an Asset to the inventory.
     */
    public void addAsset(Asset asset) {

        assets.add(asset);
    }


    /*
     * Display all assets.
     */
    public void displayAllAssets() {

        if (assets.isEmpty()) {

            System.out.println();
            System.out.println(
                    "No assets are currently stored."
            );

            return;
        }


        System.out.println();
        System.out.println(
                "=============================================================="
        );

        System.out.println(
                "                    IT ASSET INVENTORY"
        );

        System.out.println(
                "=============================================================="
        );


        System.out.printf(
                "%-10s %-12s %-25s %-20s%n",
                "ID",
                "TYPE",
                "DESCRIPTION",
                "ASSIGNED TO"
        );


        System.out.println(
                "--------------------------------------------------------------"
        );


        for (Asset asset : assets) {

            System.out.println(
                    asset.displayInfo()
            );
        }


        System.out.println(
                "=============================================================="
        );
    }


    /*
     * Update an asset assignment.
     */
    public void updateAssignment(
            String assetId,
            String newAssignee) {

        for (Asset asset : assets) {

            if (asset.getAssetId()
                    .equalsIgnoreCase(assetId)) {

                asset.setAssignedTo(
                        newAssignee
                );

                System.out.println();

                System.out.println(
                        "Asset assignment updated successfully."
                );

                return;
            }
        }


        System.out.println();

        System.out.println(
                "Asset ID was not found."
        );
    }


    /*
     * Delete an asset.
     */
    public void deleteAsset(
            String assetId) {

        for (int i = 0;
             i < assets.size();
             i++) {

            if (assets.get(i)
                    .getAssetId()
                    .equalsIgnoreCase(assetId)) {

                assets.remove(i);

                System.out.println();

                System.out.println(
                        "Asset deleted successfully."
                );

                return;
            }
        }


        System.out.println();

        System.out.println(
                "Asset ID was not found."
        );
    }
}
