package com.example.work3;

import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.time.LocalDateTime;

public class WorkException extends Exception
{

    private static String error_fileName= "Errors_message.txt";;
    private String info;




    public WorkException(String info)
    {
        super(info);
        error_fileName= "Errors_message.txt";


    }


    public void FileError(String error_info)
    {

        try
        {

                Writer Input = new FileWriter("Errors_message.txt",true);
                String error = LocalDateTime.now() + ",TYPE OF ERROR: "+error_info+"\n";
                Input.write(error);
                Input.close();

        }
        catch(IOException Exeption)
        {

            System.out.println(Exeption.getLocalizedMessage());
        }
        catch(NullPointerException Exeption)
        {

            System.out.println(Exeption.getLocalizedMessage());
        }



    }
}
