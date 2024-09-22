package com.example.work3;

import javafx.scene.control.Alert;

import java.text.SimpleDateFormat;
import java.util.Date;
public class Spectacle implements Comparable<Spectacle> {
    private String piece_name;
    private String author;
    private String theatre;
    private Date performance_date;
    private Integer act_quantity;
    private Float prise_ticket;
    private Boolean music;
    final static  SimpleDateFormat form = new SimpleDateFormat("dd/MM/yyyy");
    static final String[] spectacle_field = {"Name","Author","Theatre","Performance_Date","Quantity_of_acts","Ticket_price","Music"};
    static int[] spectacle_order = new int[7];
    public static void SETindexParam(String parameters)
    {
        String[] parameter = parameters.split(",");
        for(int i = 0; i < spectacle_field.length; ++i) {
            for(int j = 0; j < parameter.length; ++j) {
                if(parameter[j].equals(spectacle_field[i])) {

                    spectacle_order[i] = j;
                    break;
                }

            }
        }
    }

    public Spectacle(){

    }


    public Spectacle(String parameters) throws Exception
    {
        if(parameters == null)
            throw new WorkException("EMPTY PARAMETERS");

        String[] parameter = parameters.split(",");



        SET_piece_name(parameter[spectacle_order[0]]);

        SET_author(parameter[spectacle_order[1]]);

        SET_theatre(parameter[spectacle_order[2]]);

        SET_performance_date(parameter[spectacle_order[3]]);

        SET_act_quantity(parameter[spectacle_order[4]]);

        SET_prise_ticket(parameter[spectacle_order[5]]);

        SET_music(parameter[spectacle_order[6]]);


    }



    public static SimpleDateFormat GET_date_form()
    {
        return form;
    }



    public String GET_piece_name()
    {
        return piece_name;
    }


    public void SET_piece_name(String piece_name) throws Exception
    {
        if (piece_name.length() == 0)
        {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error");
            alert.setHeaderText(null);
            alert.setContentText("INCORRECT PIECE NAME: ITS CANT BE EMPTY");
            alert.showAndWait();


            throw new Exception("INCORRECT PIECE NAME: ITS CANT BE EMPTY");


        }
        this.piece_name = piece_name;
    }

    public String GET_author()
    {
        return author;
    }

    public void SET_author(String author) throws Exception
    {
        if (author.length() == 0)
        {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error");
            alert.setHeaderText(null);
            alert.setContentText("INCORRECT AUTHOR: ITS CANT BE EMPTY");
            alert.showAndWait();
            throw new Exception("INCORRECT AUTHOR: ITS CANT BE EMPTY");
        }
        this.author = author;
    }

    public String GET_theatre()
    {
        return theatre;
    }

    public void SET_theatre(String theatre) throws Exception
    {
        if (theatre.length() == 0)
        {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error");
            alert.setHeaderText(null);
            alert.setContentText("INCORRECT THEATRE: ITS CANT BE EMPTY");
            alert.showAndWait();
            throw new Exception("INCORRECT THEATRE: ITS CANT BE EMPTY");
        }
        this.theatre = theatre;
    }

    public Date GET_performance_date()
    {

        return performance_date;
    }


    public void SET_performance_date(String performance_date) throws Exception {
        try {
            this.performance_date = form.parse(performance_date);
        }
        catch (Exception ex)
        {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error");
            alert.setHeaderText(null);
            alert.setContentText("INCORRECT PERFORMANCE DATE");
            alert.showAndWait();
            throw new Exception(ex.getLocalizedMessage() + " INCORRECT PERFORMANCE DATE");
        }
    }

    public Integer GET_act_quantity()
    {
        return act_quantity;
    }

    public void SET_act_quantity(String act_quantity) throws Exception
    {
        if (act_quantity.length() == 0)
        {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error");
            alert.setHeaderText(null);
            alert.setContentText("INCORRECT ACT QUANTITY: ITS CANT BE 0");
            alert.showAndWait();
            throw new Exception("INCORRECT ACT QUANTITY: ITS CANT BE 0");
        }
        try
        {
            this.act_quantity = (Integer.parseInt(act_quantity));
        }
        catch (Exception ex) {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error");
            alert.setHeaderText(null);
            alert.setContentText("INCORRECT ACT QUANTITY: MUST BE A NUMBER");
            alert.showAndWait();
            throw new Exception("INCORRECT ACT QUANTITY: MUST BE A NUMBER");
        }
    }

    public Float GET_prise_ticket()
    {

        return prise_ticket;
    }

    public void SET_prise_ticket(String prise_ticket) throws Exception
    {
        try {
            this.prise_ticket = (Float.parseFloat(prise_ticket));
            if (prise_ticket.length() == 0)
            {
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setTitle("Error");
                alert.setHeaderText(null);
                alert.setContentText("INCORRECT PRICE OF TICKET: ITS CANT BE 0");
                alert.showAndWait();
                throw new Exception("INCORRECT PRICE OF TICKET: ITS CANT BE 0");
            }
        }
        catch (NumberFormatException Exeption)
        {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error");
            alert.setHeaderText(null);
            alert.setContentText("INCORRECT PRICE OF TICKET: MUST BE A NUMBER");
            alert.showAndWait();
            throw new Exception("INCORRECT PRICE OF TICKET: MUST BE A NUMBER");
        }


    }

    public Boolean GET_music()
    {
        return music;
    }
    public void SET_music(Boolean music)
    {

        this.music = music;
    }

    public void SET_music(String music) throws Exception

    {

        SET_music(Boolean.parseBoolean(music));

    }


    @Override
    public int compareTo(Spectacle S) {
        int res = this.piece_name.compareTo(S.piece_name);
        if(res == 0)
        {
            Integer temp = this.act_quantity;
            res = temp.compareTo(S.act_quantity);
        }
        return res;
    }


    @Override
    public String toString() {
        return "Name: " + piece_name  +
                ", Author: " + author +
                ", Theatre: " +  theatre+
                ", Performance date: " + performance_date+
                ", Quantity of acts: " +  act_quantity+
                ", Ticket price: " + prise_ticket+
                ", Music: " +  music ;

    }


    public String toJson() {
        return ("\"Name\": \'" + piece_name  + '\'' +
                ", \"Author\": \'" + author + '\'' +
                ", \"Theatre\": \'" +  theatre+ '\'' +
                ", \"Performance date\": \'" + performance_date+ '\'' +
                ", \"Quantity of acts\": " +  act_quantity +
                ", \"Ticket price\": " + prise_ticket +
                ", \"Music\": " +  music);

    }
}
