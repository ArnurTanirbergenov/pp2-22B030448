package lab1;

import java.util.Scanner;

public class deposit {
	public static void main(String args[]) {
		Scanner input = new Scanner(System.in);
		
		int balance;
		int interest;
		
		System.out.println("Write your balance: ");
		balance = input.nextInt();
		
		System.out.println("Write an interest: ");
		interest = input.nextInt();
		
		balance = balance + (balance * interest)/ 100 ;
		
		System.out.println("Your balance now is: " + balance);
	}
}
