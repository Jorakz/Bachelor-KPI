package com.example.work_2;
import java.io.FileWriter;
import java.net.URL;
import java.time.LocalDateTime;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.scene.control.ListView;
import java.util.stream.Collectors;
import java.io.File;


import javafx.scene.control.Button;
import javafx.stage.FileChooser;


public class Error_Controller {

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private Button save_button;

    @FXML
    private ListView<String> view_error;
    public void Save_log()
    {

        FileChooser file_log = new FileChooser();
        File file_d = file_log.showSaveDialog(Main_Controller.main_stage);
        if (file_d == null)
        {
            return;
        }
        try{
            String log_info = view_error.getItems().stream().map(Object::toString).collect(Collectors.joining("\n"));
            String path = file_d.getAbsolutePath();
            view_error.getItems().add(LocalDateTime.now() + " - SAVE LOG IN FILE '"+path+"'");
            System.out.println(LocalDateTime.now() + " - SAVE LOG IN FILE '"+path+"'");
            FileWriter input_log_info = new FileWriter(path,false);
            input_log_info.write(log_info);
            input_log_info.close();
        }
        catch(Exception ex)
        {

        }
    }
    public void addListView(String info) {
        view_error.getItems().add(LocalDateTime.now() + " - "+ info);
    }

    public void addListView_error(Exception ex) {
        view_error.getItems().add(LocalDateTime.now() + " - "+ ex.getMessage());
        save_button.setOnAction(actionEvent -> Save_log());
    }

    @FXML
    void initialize() {
    }
}
