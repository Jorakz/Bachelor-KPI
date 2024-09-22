package com.example.work3;

import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.AnchorPane;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import java.sql.*;
import java.sql.Connection;

import java.io.File;
import java.io.IOException;

import java.util.ArrayList;
import java.util.stream.Collectors;




public class Main_Controller {


    @FXML
    private TextField Author_input;

    @FXML
    private AnchorPane Main_Window;

    @FXML
    private TextField Music_input;

    @FXML
    private TextField Name_input;

    @FXML
    private TextField Performance_input;

    @FXML
    private TextField Price_input;

    @FXML
    private TextField Quantity_input;

    @FXML
    private TextField Theatre_input;

    @FXML
    private ComboBox<String> box_search;

    @FXML
    private Button button_add;

    @FXML
    private Button button_save;

    @FXML
    private Button button_update;

    @FXML
    private Button button_add_elem;

    @FXML
    private Button button_delete_all_elem;

    @FXML
    private Button button_delete_elem;

    @FXML
    private TextField search_input;

    @FXML
    private ListView<Spectacle> view_data;

    private static Container_Spectacle container_spect = new Container_Spectacle();
    public static Stage main_stage = null;
    private static Spectacle spect = null;
    private static Error_Controller error_log = null;
    private static Connection connection;
    public static String url ;
    public static String username;
    public static String password ;



    private void Output_CSV() {

        FileChooser file_choose = new FileChooser();
        File file = file_choose.showOpenDialog(main_stage);

        try {
            String path = file.getAbsolutePath();
            error_log.addListView("READING DATAS FROM FILE '" + path + "'");

            container_spect.Output(path);

        } catch (Exception ex) {

            error_log.addListView_error(ex);

        }
        view_data.setItems(FXCollections.observableList(container_spect.GET_arraylist()));
        for(Spectacle spect  : container_spect.GET_arraylist())
            Spect_add_db((ID_Spectacle) spect);
    }

    private void Error_log() throws IOException {
        try {
            FXMLLoader fxml = new FXMLLoader(getClass().getResource("view_error_log.fxml"));
            Stage stage = new Stage();
            stage.setScene(new Scene(fxml.load()));
            stage.setResizable(false);
            stage.show();
            error_log = fxml.getController();
        } catch (IOException exception) {

        }
    }

    private void Input_JSON() {
        FileChooser file_c = new FileChooser();
        File file = file_c.showSaveDialog(main_stage);
        if (file == null) {
            return;
        }
        try {
            String path = file.getAbsolutePath();
            container_spect.Input_json(file.getAbsolutePath());
            error_log.addListView("SAVE DATA IN JSON FILE '" + path + "'");

        } catch (Exception ex) {
            error_log.addListView_error(ex);

        }

    }

    private void Fill_spect() {
        if (spect == null)
            return;

        Name_input.setText(spect.GET_piece_name());
        Author_input.setText(spect.GET_author());
        Theatre_input.setText(spect.GET_theatre());
        Performance_input.setText(Spectacle.form.format(spect.GET_performance_date()));
        Quantity_input.setText(spect.GET_act_quantity().toString());
        Price_input.setText(spect.GET_prise_ticket().toString());
        Music_input.setText(spect.GET_music().toString());
        view_data.setItems(FXCollections.observableList(container_spect.GET_arraylist()));

    }

    private void Spect_select() {

        spect = view_data.getSelectionModel().getSelectedItem();
        Fill_spect();

    }

    private void Spect_save_db(ID_Spectacle spectacle)
    {
        String save_spect = "UPDATE spectacle_tabl SET Name = ?,Author = ?,Theatre = ?,Performance_Date = ?,Quantity_of_acts = ?,Ticket_price = ?,Music = ? WHERE ID = ?";
        try(Connection conn = Connect_db(url, username, password);
            PreparedStatement Stat = conn.prepareStatement(save_spect))
        {

            Stat.setString(1,spectacle.GET_piece_name());
            Stat.setString(2,spectacle.GET_author());
            Stat.setString(3,spectacle.GET_theatre());
            Stat.setString(4,spectacle.GET_date_form().format(spectacle.GET_performance_date()));
            Stat.setInt(5,spectacle.GET_act_quantity());
            Stat.setFloat(6,spectacle.GET_prise_ticket());
            Stat.setString(7,spectacle.GET_music().toString());
            Stat.setInt(8,spectacle.GET_id());
            Stat.executeUpdate();
        }
        catch(SQLException ex)
        {
            error_log.addListView(
                    "Failed to update show data.");
        }
    }
    private void Spect_save() {
        if (spect == null)
            return;
        try {
            Spectacle s = spect;
            spect.SET_piece_name(Name_input.getText());
            spect.SET_author(Author_input.getText());
            spect.SET_theatre(Theatre_input.getText());
            spect.SET_performance_date(Performance_input.getText());
            spect.SET_act_quantity(Quantity_input.getText());
            spect.SET_prise_ticket(Price_input.getText());
            spect.SET_music(Music_input.getText());
            error_log.addListView("SPECTACLE DATA ID("+ ((ID_Spectacle)spect).GET_id()+") HAS BEEN CHANGED");

        } catch (Exception ex) {
            error_log.addListView_error(ex);

        }
        view_data.setItems(FXCollections.observableList(container_spect.GET_arraylist()));
        Fill_spect();
        Spect_save_db((ID_Spectacle) spect);
    }

    private void Spect_search() {
        ArrayList<Spectacle> arr = container_spect.GET_arraylist();
        if (search_input.getText().equals("")) {
            view_data.setItems(FXCollections.observableList(container_spect.GET_arraylist()));
            return;
        }
        switch (box_search.getSelectionModel().getSelectedItem().toString()) {
            case ("Name"):

                arr = (ArrayList<Spectacle>) container_spect.GET_arraylist().stream().filter(ar -> ar.GET_piece_name().toLowerCase().contains(search_input.getText().toLowerCase())).collect(Collectors.toList());
                error_log.addListView("SEARCH FOR '" + search_input.getText() + "' IN CASE 'Name'");

                break;
            case ("Author"):
                arr = (ArrayList<Spectacle>) container_spect.GET_arraylist().stream().filter(ar -> ar.GET_author().toLowerCase().contains(search_input.getText().toLowerCase())).collect(Collectors.toList());
                error_log.addListView("SEARCH FOR '" + search_input.getText() + "' IN CASE 'Author'");

                break;
            case ("Theatre"):
                arr = (ArrayList<Spectacle>) container_spect.GET_arraylist().stream().filter(ar -> ar.GET_theatre().toLowerCase().contains(search_input.getText().toLowerCase())).collect(Collectors.toList());
                error_log.addListView("SEARCH FOR '" + search_input.getText() + "' IN CASE 'Theatre'");

                break;
            case ("Performance_Date"):
                arr = (ArrayList<Spectacle>) container_spect.GET_arraylist().stream().filter(ar -> ar.GET_performance_date().toString().toLowerCase().contains(search_input.getText().toLowerCase())).collect(Collectors.toList());
                error_log.addListView("SEARCH FOR '" + search_input.getText() + "' IN CASE 'Performance_Date'");

                break;
            case ("Ticket_price"):
                arr = (ArrayList<Spectacle>) container_spect.GET_arraylist().stream().filter(ar -> ar.GET_prise_ticket().toString().toLowerCase().contains(search_input.getText().toLowerCase())).collect(Collectors.toList());
                error_log.addListView("SEARCH FOR '" + search_input.getText() + "' IN CASE 'Ticket_price'");

                break;
            case ("Music"):
                arr = (ArrayList<Spectacle>) container_spect.GET_arraylist().stream().filter(ar -> ar.GET_music().toString().toLowerCase().contains(search_input.getText().toLowerCase())).collect(Collectors.toList());
                error_log.addListView("SEARCH FOR '" + search_input.getText() + "' IN CASE 'Music'");

                break;
            case ("Quantity_of_acts"):
                arr = (ArrayList<Spectacle>) container_spect.GET_arraylist().stream().filter(ar -> ar.GET_act_quantity().toString().toLowerCase().contains(search_input.getText().toLowerCase())).collect(Collectors.toList());
                error_log.addListView("SEARCH FOR '" + search_input.getText() + "' IN CASE 'Quantity_of_acts'");

                break;
        }
        view_data.setItems(FXCollections.observableList(arr));

    }
    private void Spect_delete_db(int ID)
    {
        String delete_spectacle = "DELETE FROM spectacle_tabl WHERE ID = ?";
        try(Connection conn = Connect_db(url, username, password);
            PreparedStatement Stat = conn.prepareStatement(delete_spectacle))
        {
            Stat.setInt(1,ID);
            Stat.executeUpdate();
        }
        catch (SQLException ex)
        {
            error_log.addListView("Failed to delete show data.");
        }
    }
    private void Spect_delete() {
        Alert alert = new Alert(Alert.AlertType.CONFIRMATION);

        alert.setTitle("Видалення об'єкту");
        alert.setHeaderText("Видалити обраний об'єкт з бази?");
        if (alert.showAndWait().get() != ButtonType.OK) {
            return;
        }

        if (spect == null) {
            return;
        }
        error_log.addListView("DELETE DATA OF SPECTALCE ID ("+((ID_Spectacle)spect).GET_id()+")");
        Spect_delete_db(((ID_Spectacle)spect).GET_id());
        container_spect.GET_arraylist().remove(spect);
        view_data.setItems(FXCollections.observableList(container_spect.GET_arraylist()));
        spect = null;

    }

    private void Delete_all() {
        Alert alert = new Alert(Alert.AlertType.CONFIRMATION);

        alert.setTitle("Очищення бази даних");
        alert.setHeaderText("Видалити всі об'єкти з бази?");
        if (alert.showAndWait().get() != ButtonType.OK) {
            return;
        }
        error_log.addListView("DELETING ALL DATA FROM THE SPECTACLE DATABASE");
        container_spect.GET_arraylist().clear();
        String delete_all_spect = "DROP TABLE IF EXISTS spectacle_tabl";
        try(Connection conn = Connect_db(url, username, password);
            Statement Stat = conn.createStatement())
        {
            Stat.executeUpdate(delete_all_spect);

        }
        catch(SQLException e)
        {
            error_log.addListView("Failed to delete all spectacle data");
        }

        view_data.setItems(FXCollections.observableList(container_spect.GET_arraylist()));

    }
    private void Spect_add_db(ID_Spectacle spectacle)
    {
        String add_spectacle = "INSERT INTO spectacle_tabl(ID,Name,Author,Theatre,Performance_Date,Quantity_of_acts,Ticket_price,Music) VALUES (?,?,?,?,?,?,?,?)";

        try(Connection conn = Connect_db(url, username, password);
            PreparedStatement Stat = conn.prepareStatement(add_spectacle))
        {
            Stat.setInt(1,spectacle.GET_id());
            Stat.setString(2,spectacle.GET_piece_name());
            Stat.setString(3,spectacle.GET_author());
            Stat.setString(4,spectacle.GET_theatre());
            Stat.setString(5,spectacle.GET_date_form().format(spectacle.GET_performance_date()));
            Stat.setInt(6,spectacle.GET_act_quantity());
            Stat.setFloat(7,spectacle.GET_prise_ticket());
            Stat.setString(8,spectacle.GET_music().toString());
            Stat.executeUpdate();

        }
        catch(SQLException e)
        {

        }
    }
    public void Spect_adding()
    {

        Spect_add();
        error_log.addListView("ADDING NEW SPECTACLE DATA WITH ID ("+((ID_Spectacle)spect).GET_id()+")");

    }
    private void Spect_add() {

        spect = null;
        Spectacle.SETindexParam("Name,Author,Theatre,Performance_Date,Quantity_of_acts,Ticket_price,Music");
        StringBuilder new_spectacle = new StringBuilder();
        new_spectacle.append(Name_input.getText()).append(',').
                append(Author_input.getText()).append(',').
                append(Theatre_input.getText()).append(',').
                append(Performance_input.getText()).append(',').
                append(Quantity_input.getText()).append(',').
                append(Price_input.getText()).append(',').
                append(Music_input.getText());
        try {
            ID_Spectacle spectacle = new ID_Spectacle(new_spectacle.toString());
            Spect_add_db(spectacle);
            container_spect.GET_arraylist().add(spectacle);
            view_data.setItems(FXCollections.observableList(container_spect.GET_arraylist()));
            spect = spectacle;
            view_data.getSelectionModel().selectLast();
        } catch (Exception ex) {
            error_log.addListView_error(ex);

        }


    }


    @FXML
    void initialize() throws IOException {

        Error_log();
        Database_loading();

        box_search.getItems().addAll("Name", "Author", "Theatre", "Performance_Date", "Quantity_of_acts", "Ticket_price", "Music", "-");
        button_update.setOnAction(actionEvent -> Output_CSV());
        button_add.setOnAction(actionEvent -> Input_JSON());
        view_data.setOnMouseClicked(mouseEvent -> Spect_select());
        button_save.setOnAction(actionEvent -> Spect_save());
        box_search.setOnAction(actionEvent -> Spect_search());
        button_delete_elem.setOnAction(actionEvent -> Spect_delete());
        button_delete_all_elem.setOnAction(actionEvent -> Delete_all());
        button_add_elem.setOnAction(actionEvent -> Spect_adding());
    }

    static public Connection Connect_db(String url, String username, String password) {
        Connection connection = null;
        try {
            connection = DriverManager.getConnection(url, username, password);

        } catch (SQLException e) {

            error_log.addListView("Failed to connect to databese spectacle data");
        }

        return connection;

    }

    private void CreateTable_db(String url, String username, String password) {
        String create_spectacle = """
                CREATE TABLE IF NOT EXISTS spectacle_tabl( ID integer PRIMARY KEY, Name varchar(45),Author varchar(45),Theatre varchar(45),Performance_Date varchar(45),Quantity_of_acts int,Ticket_price float,Music varchar(45));""";
        String create_logs = """
                CREATE TABLE IF NOT EXISTS log_tabl(data varchar(45) PRIMARY KEY,message varchar(150));""";
        try {
            Connection conn = Connect_db(url, username, password);
            Statement stmt = conn.createStatement();
            stmt.execute(create_spectacle);
            stmt.execute(create_logs);

        } catch (SQLException ex) {
        }
    }

    private void Select_db(String url, String username, String password, String filters)
    {
        String select_spect = "SELECT * FROM spectacle_tabl" + filters;
        try(Connection conn = Connect_db(url, username, password);
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(select_spect)){
            Spectacle.SETindexParam("Name,Author,Theatre,Performance_Date,Quantity_of_acts,Ticket_price,Music");
            while(rs.next())
            {
                StringBuilder param_str = new StringBuilder();
                for (String param_name : Spectacle.spectacle_field) {
                    param_str.append(rs.getString(param_name)).append(',');
                }
                ID_Spectacle spectacle = new ID_Spectacle(param_str.toString());
                spectacle.SET_ID(rs.getInt("id"));
                container_spect.GET_arraylist().add(spectacle);


            }

        }
        catch(SQLException ex)
        {

        }
        catch (Exception ex)
        {
            error_log.addListView_error(ex);
        }

    }

    private void Set_maximum_ID_db(String url, String username, String password)
    {
        String max_id = "SELECT MAX(id) From spectacle_tabl";
        try(Connection conn = Connect_db(url, username, password);
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(max_id))
        {
            rs.next();
            ID_Spectacle.SET_ID_start(rs.getInt(1)+1);

            }

        catch(SQLException ex)
        {
            error_log.addListView("Failed to find max id of spectacle ID");
        }

    }

    private void Select_log_db(String url, String username, String password)
    {

        String select_logs = "SELECT * FROM log_tabl";

        try(Connection conn = Connect_db(url, username, password);
            Statement Stat = conn.createStatement();
            ResultSet rs = Stat.executeQuery(select_logs))

        {
            while(rs.next())
            {




                try{error_log.addListView_db(rs.getString(2),rs.getString(1));}
                catch(SQLException ignore)
                {

                }
                catch (Exception ex)
                {
                    error_log.addListView_error(ex);

                }
            }
        }
        catch (SQLException ex)
        {

        }
    }

    private void Database_loading()
    {

        try {
            Class.forName("com.mysql.cj.Driver");
        }
            catch(ClassNotFoundException ex)
        {

        }
        Connect_db(url,username,password);
        CreateTable_db(url,username,password);
        Select_db(url,username,password, "");
        Set_maximum_ID_db(url,username,password);
        Select_log_db(url,username,password);

    }
}

