import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main  extends Application {
    private static String url;
    private static int port;
    private static String username;
    private static String password;
    private static String local_dir;
    private static String remote_dir;

    public static void main(String[] args) {
        url = "195.3.158.22";
        port = 8000;
        username = "03-06";
        password = "P1Fqjp";
        local_dir = "images";
        remote_dir = "lab5";

        launch(args);
    }

    @Override
    public void start(Stage stage) throws Exception {
        FXMLLoader loaderMain = new FXMLLoader(getClass().getClassLoader().getResource("Main_window.fxml"));
        Parent rootMain = loaderMain.load();
        Scene sceneMain = new Scene(rootMain, 750, 420);
        Controller controller = loaderMain.getController();
        controller.initialize(url, port, username, password, local_dir, remote_dir);
        stage.setTitle("5 ЛАБОРОТОРНА РОБОТА - Затуловський");

        stage.setScene(sceneMain);

        stage.show();
    }

}