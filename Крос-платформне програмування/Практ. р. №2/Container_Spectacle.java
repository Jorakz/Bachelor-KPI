package com.example.work_2;
import java.util.Collections;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.IOException;
import java.io.File;
import java.io.FileWriter;

public class Container_Spectacle   {
    public ArrayList<Spectacle> Constain = new ArrayList<>();

    public Container_Spectacle(){}

    public void Output(String name) throws Exception {
        try{
            File file = new File (name);
            Scanner scan_file = new Scanner(file);
            String[] parametrs = scan_file.nextLine().split(",");
            int counter = 1;
            while(scan_file.hasNextLine())
            {
                counter+=1;
                try{
                    String data = scan_file.nextLine();
                    Spectacle spectacle = new ID_Spectacle(data, parametrs);
                    Constain.add(spectacle);

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
