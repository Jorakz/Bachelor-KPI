package com.example.work3;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;


public class Container_Spectacle   {
    public ArrayList<Spectacle> Constain = new ArrayList<>();

    public Container_Spectacle(){}

    public void Output(String name) throws Exception {
        try{
            FileReader file = new FileReader (name);
            BufferedReader buff_file = new BufferedReader(file);
            String head = buff_file.readLine();
            Spectacle.SETindexParam(head);
            String spect_line;
            int counter = 1;
            while((spect_line = buff_file.readLine())!=null)
            {
                counter+=1;
                try{
                    Spectacle spect = new ID_Spectacle(spect_line);
                    Constain.add(spect);

                }

                catch(WorkException Exeption){
                    Exeption.FileError(" ERROR IN READING CSV FILE IN ROW #" + counter +" : "+ Exeption.getLocalizedMessage());
                }



            }

        }
        catch(IOException Exeption)
        {
            throw new WorkException(Exeption.getLocalizedMessage());
        }

    }


    public void Input_json(String name) throws WorkException {
        try(FileWriter Input_in_file = new FileWriter(name)) {
            String text = "[\n";
            for(int i = 0; i < Constain.size(); i++)
            {
                text = text + " {" + (Constain.get(i).toJson()) + " }";
                if(i != (Constain.size() - 1) )
                    text = text + ",";
                text = text + "\n";
            }
            text += "]";

            Input_in_file.write(text);
            Input_in_file.flush();
        }
        catch(IOException Exeption)
        {
            throw new WorkException(Exeption.getLocalizedMessage());
        }
    }
    public ArrayList<Spectacle> GET_arraylist()
    {
        return Constain;
    }

    @Override
    public String toString() {
        return "Spectacle : { " + Constain + "}";
    }


    public void Sort(){
        Collections.sort(Constain);
    }
}
