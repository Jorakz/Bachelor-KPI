package com.example.work_2;
public class ID_Spectacle extends Spectacle {
    private static int id_static = 0;
    private int id = 0;
    public ID_Spectacle() {
        this.id = ++id_static;
    }

    public ID_Spectacle(String parametrs, String[] value) throws Exception {
        super(parametrs,value);
        this.id = ++id_static;
    }
    public int GET_id() {
        return id;
    }


    @Override
    public String toString() {

        return "{ID: " + GET_id() +", "+ super.toString()+"}\n";
    }

    @Override
    public String toJson(){
        return ("\"ID\": " + id + ", " + super.toJson());
    }





}
