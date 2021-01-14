package com.java;
import java.util.*;
import java.lang.Math;

public class one {

  public static void main(String[] args) {
System.out.println("SQUARE ROOT CALCULATOR");
System.out.println("Only upto 14 digits");
Scanner sc = new Scanner(System.in);
while(true){
System.out.println("");
System.out.println("Enter the no. for square root: ");
String str= sc.nextLine();
Double number = Double.parseDouble(str);
System.out.println("");
System.out.println(Math.sqrt(number));
       }


  
  
  
  }

}
