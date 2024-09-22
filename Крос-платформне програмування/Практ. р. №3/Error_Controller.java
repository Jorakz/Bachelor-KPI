package com.example.work3;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.stage.FileChooser;

import java.io.File;
import java.io.FileWriter;
import java.net.URL;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Statement;
import java.time.LocalDateTime;
import java.util.ResourceBundle;
import java.util.stream.Collectors;


public class Error_Controller {

    @FXML
    private Button delete_button;

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
            addListView("SAVE ALL DATA FROM THE LOG DATABASE INTO "+path);
            FileWriter input_log_info = new FileWriter(path,false);
            input_log_info.write(log_info);
            input_log_info.close();
        }
        catch(Exception ex)
        {

        }
    }
    public void Add_log_db(String log_info,String date_m)
    {

        String add_log= "INSERT INTO log_tabl(data, message) VALUES(?, ?)";
        try(Connection conn = Main_Controller.Connect_db(Main_Controller.url,Main_Controller.username,Main_Controller.password);
            PreparedStatement Stat = conn.prepareStatement(add_log))
        {

            Stat.setString(1,date_m);
            Stat.setString(2,log_info);
            Stat.executeUpdate();
        }
        catch(SQLException ex)
        {

        }

    }
    public void Delete_log_db()
    {
        String delete_all_log = "DROP TABLE IF EXISTS log_tabl";
        try(Connection conn = Main_Controller.Connect_db(Main_Controller.url,Main_Controller.username,Main_Controller.password);
            Statement Stat = conn.createStatement())
        {
            Stat.executeUpdate(delete_all_log);

        }
        catch(SQLException e)
        {
            view_error.getItems().add("Не вдалось видалити всі дані з журналу");
        }
    }
    public void Delete_log()
    {
        addListView("DELETING ALL DATA FROM THE LOG DATABASE");
        view_error.getItems().clear();
        Delete_log_db();
    }
    public void addListView(String info) {
        String date_m = LocalDateTime.now().toString();
        view_error.getItems().add(date_m + " - "+ info);
        Add_log_db(info,date_m);
    }

    public void addListView_db(String info_,String date_)
    {
        view_error.getItems().add(date_+ " - "+ info_);
        Add_log_db(info_,date_);
    }

    public void addListView_error(Exception ex) {
        String date_er = LocalDateTime.now().toString();
        view_error.getItems().add(date_er  + " - "+ ex.getMessage());

        Add_log_db(ex.getMessage(),date_er);

    }


    @FXML
    void initialize() {

        save_button.setOnAction(actionEvent -> Save_log());
        delete_button.setOnAction(actionEvent -> Delete_log());
    }
}
