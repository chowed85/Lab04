/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author aaronvuong
 */
import java.net.*;
import java.nio.ByteBuffer;
import java.util.Scanner;
import java.util.Random;

public class UDPSender {

	public static void main(String[] args) 
   {
	      // Check the arguments
	      if( args.length != 2 )
	      {
	         System.out.println( "usage: java UDPSender host port" ) ;
	         return ;
	      }
	      DatagramSocket socket = null ;
	      try
	      {
	         // Convert the arguments first, to ensure that they are valid
	         InetAddress host  = InetAddress.getByName( args[0] ) ;
	         int port          = Integer.parseInt( args[1] ) ;

	         socket = new DatagramSocket() ;
     
	         Scanner in;
	         in = new Scanner (System.in);
	         int message;
                 Random r = new Random();

	         while (true)
	         {
				
	        		 System.out.println("ENTER to quit ");
				 for(int i=0; i<10;i++){
	        		 message = r.nextInt();
                                 ByteBuffer b = ByteBuffer.allocate(4);
                                 b.putInt(message);
	        		 byte [] data = b.array();
	        		 DatagramPacket packet = new DatagramPacket( data, data.length, host, port ) ;
	        		 socket.send( packet ) ;                       
}
break;
	         } 
	         System.out.println ("Closing down");
	      }
	      catch( Exception e )
	      {
	         System.out.println( e ) ;
	      }
	      finally
	      {
	         if( socket != null )
	            socket.close() ;
      }
   }
}
