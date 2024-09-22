package com.example.work_2;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class Main_Application extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(Main_Application.class.getResource("view-main.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 706, 483);
        stage.setResizable(false);
        stage.setScene(scene);
        Main_Controller.main_stage = stage;
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}