package learning;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.nio.charset.StandardCharsets;


public class aranea_splitter {

	public static void main(String[] args) throws Exception {
		try{
			
			BufferedReader reader = new BufferedReader(
	                new InputStreamReader(
	                        new FileInputStream("C:\\Users\\kamivao\\Downloads\\ru_ar_cut.txt"), StandardCharsets.UTF_8));
			Writer writer = new BufferedWriter(new OutputStreamWriter(
		              new FileOutputStream("C:\\Users\\kamivao\\Downloads\\ru_aranea_sample_lemmas.txt"), "utf-8")); 
		
			
			String lineJustFetched = reader.readLine();
			int count = 0;
			
			
			while (lineJustFetched != null){
				
				
				if(lineJustFetched.contains(Character.toString('<'))) {
					lineJustFetched = reader.readLine();}
				
					
					
				else{
					String[] tokens = lineJustFetched.split("\t");
					writer.write(tokens[1] + " ");
					count++;
					lineJustFetched = reader.readLine();
				}
		
			}
				
				reader.close();
				writer.close();
				System.out.println("Number of lexemes = " + count);
			
			
		}
		catch (FileNotFoundException e) {
		        System.err.println("Unable to find the file: fileName");
		    } 
		catch (IOException e) {
		        System.err.println("Unable to read the file: fileName");
		    	}
			
		}
	
}


