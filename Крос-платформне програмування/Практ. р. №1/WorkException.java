import java.io.FileWriter;

import java.io.IOException;
import java.time.LocalDateTime;

public class WorkException extends Exception
{

    private static String error_fileName;
    private String error_info;

    /**
     *
     * @param info contains error messages
     *
     */
    public WorkException(String info)
    {
        super(info);
        error_fileName= "Errors.log";


    }

    /**
     * A method of writing an error message while the program is running
     * @param error contains the error message
     */
    public void FileError(String error)
    {
        try
        {
            if(error_fileName != null){
                FileWriter Input = new FileWriter(error_fileName,true);
                Input.write( "TIME OF ERROR: "+LocalDateTime.now() + ",TYPE OF ERROR: "+error_info+" "+error+"\n");
                Input.close();
            }
            else
            {
                throw new NullPointerException(" FILE NAME IS EMPTY\n");
            }
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
