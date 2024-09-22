package com.example.work_2;

import java.io.IOException;
import java.util.ArrayList;
import java.io.File;
import javafx.scene.Scene;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import java.util.stream.Collectors;
import javafx.fxml.FXMLLoader;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;



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
    private TextField search_input;

    @FXML
    private ListView<Spectacle> view_data;

    private static Container_Spectacle container_spect = new Container_Spectacle();
    public static Stage main_stage = null;
    private static Spectacle spect = null;
    private static Error_Controller error_log = null;


    private void Output_CSV(){

        FileChooser file_choose = new FileChooser();
        File file = file_choose.showOpenDialog(main_stage);

        try{
            String path = file.getAbsolutePath();
            error_log.addListView("READING DATAS FROM FILE '" + path + "'");
            System.out.println("READING DATAS FROM FILE '" + path + "'");
            container_spect.Output(path);

        } catch (Exception ex) {

            error_log.addListView_error(ex);
            System.out.println(ex);
        }
        view_data.setItems(FXCollections.observableList(container_spect.GET_arraylist()));

    }

    private void Error_log() throws IOException{
        try {
            FXMLLoader fxml = new FXMLLoader(getClass().getResource("view-error.fxml"));
            Stage stage = new Stage();
            stage.setScene(new Scene(fxml.load()));
            stage.setResizable(false);
            stage.show();
            error_log = fxml.getController();
        } catch (IOException exception) {

        }
    }
    private void Input_JSON()
    {
        FileChooser file_c = new FileChooser();
        File file = file_c.showSaveDialog(main_stage);
        if (file == null){
            return;
        }
        try{
            String path = file.getAbsolutePath();
            container_spect.Input_json(file.getAbsolutePath());
            error_log.addListView("SAVE DATA IN JSON FILE '"+ path + "'");
            System.out.println("SAVE DATA IN JSON FILE '"+ path + "'");
        }
        catch(Exception ex)
        {
            error_log.addListView_error(ex);
            System.out.println(ex);
        }

    }
    private void Fill_spect()
    {
        if (spect == null)
            return;

        Name_input.setText(spect.GET_piece_name());
        Author_input.setText(spect.GET_author());
        Theatre_input.setText(spect.GET_theatre());
        Performance_input.setText(Spectacle.form.format(spect.GET_performance_date()));
        Quantity_input.setText(spect.GET_act_quantity().toString());
        Price_input.setText(spect.GET_prise_ticket().toString());
        Music_input.setText(spect.GET_music().toString());

    }
    private void Spect_select()
    {

        spect = view_data.getSelectionModel().getSelectedItem();
        Fill_spect();

    }
    private void Spect_save()
    {
        if (spect == null)
            return;
        try{
            Spectacle s = spect;
            spect.SET_piece_name(Name_input.getText());
            spect.SET_author(Author_input.getText());
            spect.SET_theatre(Theatre_input.getText());
            spect.SET_performance_date(Performance_input.getText());
            spect.SET_act_quantity(Quantity_input.getText());
            spect.SET_prise_ticket(Price_input.getText());
            spect.SET_music(Music_input.getText());
            error_log.addListView("CHANGE ITEM FROM {"+s+ "}"+" TO {"+spect + "}");
            System.out.println("CHANGE ITEM FROM {"+s+ "}"+" TO {"+spect + "}");
        }
        catch (Exception ex)
        {
            error_log.addListView_error(ex);
            System.out.println(ex);
        }
        view_data.setItems(FXCollections.observableList(container_spect.GET_arraylist()));
    }
    private void Spect_search()
    {
        ArrayList<Spectacle> arr = container_spect.GET_arraylist();
        if (search_input.getText().equals(""))
        {
            view_data.setItems(FXCollections.observableList(container_spect.GET_arraylist()));
            return;
        }
        switch (box_search.getSelectionModel().getSelectedItem().toString()){
            case ("Name"):

                arr = (ArrayList<Spectacle>) container_spect.GET_arraylist().stream().filter(ar -> ar.GET_piece_name().toLowerCase().contains(search_input.getText().toLowerCase())).collect(Collectors.toList());
                error_log.addListView("SEARCH FOR '"+ search_input.getText() + "' IN CASE 'Name'");
                System.out.println("SEARCH FOR '"+ search_input.getText() + "' IN CASE 'Name'");
                break;
            case ("Author"):
                arr = (ArrayList<Spectacle>) container_spect.GET_arraylist().stream().filter(ar -> ar.GET_author().toLowerCase().contains(search_input.getText().toLowerCase())).collect(Collectors.toList());
                error_log.addListView("SEARCH FOR '"+ search_input.getText() + "' IN CASE 'Author'");
                System.out.println("SEARCH FOR '"+ search_input.getText() + "' IN CASE 'Author'");
                break;
            case ("Theatre"):
                arr = (ArrayList<Spectacle>) container_spect.GET_arraylist().stream().filter(ar -> ar.GET_theatre().toLowerCase().contains(search_input.getText().toLowerCase())).collect(Collectors.toList());
                error_log.addListView("SEARCH FOR '"+ search_input.getText() + "' IN CASE 'Theatre'");
                System.out.println("SEARCH FOR '"+ search_input.getText() + "' IN CASE 'Theatre'");
                break;
            case ("Performance_Date"):
                arr = (ArrayList<Spectacle>) container_spect.GET_arraylist().stream().filter(ar -> ar.GET_performance_date().toString().toLowerCase().contains(search_input.getText().toLowerCase())).collect(Collectors.toList());
                error_log.addListView("SEARCH FOR '"+ search_input.getText() + "' IN CASE 'Performance_Date'");
                System.out.println("SEARCH FOR '"+ search_input.getText() + "' IN CASE 'Performance_Date'");
                break;
            case ("Ticket_price"):
                arr = (ArrayList<Spectacle>) container_spect.GET_arraylist().stream().filter(ar -> ar.GET_prise_ticket().toString().toLowerCase().contains(search_input.getText().toLowerCase())).collect(Collectors.toList());
                error_log.addListView("SEARCH FOR '"+ search_input.getText() + "' IN CASE 'Ticket_price'");
                System.out.println("SEARCH FOR '"+ search_input.getText() + "' IN CASE 'Ticket_price'");
                break;
            case ("Music"):
                arr = (ArrayList<Spectacle>) container_spect.GET_arraylist().stream().filter(ar -> ar.GET_music().toString().toLowerCase().contains(search_input.getText().toLowerCase())).collect(Collectors.toList());
                error_log.addListView("SEARCH FOR '"+ search_input.getText() + "' IN CASE 'Music'");
                System.out.println("SEARCH FOR '"+ search_input.getText() + "' IN CASE 'Music'");
                break;
            case ("Quantity_of_acts"):
                arr = (ArrayList<Spectacle>) container_spect.GET_arraylist().stream().filter(ar -> ar.GET_act_quantity().toString().toLowerCase().contains(search_input.getText().toLowerCase())).collect(Collectors.toList());
                error_log.addListView("SEARCH FOR '"+ search_input.getText() + "' IN CASE 'Quantity_of_acts'");
                System.out.println("SEARCH FOR '"+ search_input.getText() + "' IN CASE 'Quantity_of_acts'");
                break;
        }
    view_data.setItems(FXCollections.observableList(arr));
    }
    @FXML
    void initialize() throws IOException {
        Error_log();
        box_search.getItems().addAll("Name","Author","Theatre","Performance_Date","Quantity_of_acts","Ticket_price","Music","-");
        button_update.setOnAction(actionEvent -> Output_CSV());
        button_add.setOnAction(actionEvent -> Input_JSON());
        view_data.setOnMouseClicked(mouseEvent -> Spect_select());
        button_save.setOnAction(actionEvent -> Spect_save());
        box_search.setOnAction(actionEvent -> Spect_search());
    }

}