package lab1;

import java.util.Scanner;
public class palindrome {
	public static void main(String args[]) {
		Scanner input = new Scanner(System.in);
		
		String mystring;
		System.out.println("Write a word: ");
		mystring = input.nextLine();
		
		int len = mystring.length();
		char[] myCharArray = new char[len];
		
		for(int i = 0; i < mystring.length() ; i++) {
			myCharArray[i] = mystring.charAt(len - 1 - i);
		}
		String reversestring = new String(myCharArray);
		
		if(mystring.equals(reversestring))
			System.out.println("Palindrome ");
		else System.out.println("Not Palindrome ");
	}
	}
