package com.example.work3;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class Main_Application extends Application {

    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(Main_Application.class.getResource("view-main_window.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 706, 483);
        stage.setResizable(false);
        stage.setScene(scene);
        Main_Controller.main_stage = stage;

        stage.show();

    }

    public static void main(String[] args) {
        Main_Controller.url = args[0];
        Main_Controller.username =args[1];
        Main_Controller.password = args[2];
        launch();
    }
}