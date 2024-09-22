package com.example.work3;
public class ID_Spectacle extends Spectacle {
    private static int id_static = 0;
    private int id = 0;
    public ID_Spectacle() {
        this.id = ++id_static;
    }

    public ID_Spectacle(String parametrs) throws Exception {
        super(parametrs);
        this.id = ++id_static;
    }
    public int GET_id() {
        return id;
    }

    public void SET_ID(Integer id){
        this.id=id;
    }

    static public void SET_ID_start(Integer id_start)
    {
        if (id_start > id_static)
            id_start = id_static;
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
