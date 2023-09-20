package lab1;

import java.util.Scanner;

public class grading {
	public static void main(String args[]) {
		Scanner input = new Scanner(System.in);
		
		double grade;
		System.out.println("Enter a grade: ");
		grade = input.nextDouble();
		if(grade >= 95 && grade <= 100)
			System.out.println("Your grade is A ");
		if(grade >= 90 && grade <= 94)
			System.out.println("Your grade is A- ");
		if(grade >= 85 && grade <= 89)
			System.out.println("Your grade is B+ ");
		if(grade >= 80 && grade <= 84)
			System.out.println("Your grade is B ");
		if(grade >= 75 && grade <= 79)
			System.out.println("Your grade is B- ");
		if(grade >= 70 && grade <= 74)
			System.out.println("Your grade is C+ ");
		if(grade >= 65 && grade <= 69)
			System.out.println("Your grade is C ");
		if(grade >= 60 && grade <= 64)
			System.out.println("Your grade is C- ");
		if(grade >= 55 && grade <= 59)
			System.out.println("Your grade is D+ ");
		if(grade >= 50 && grade <= 54)
			System.out.println("Your grade is D ");
		if(grade >= 30 && grade <= 49)
			System.out.println("Your grade is FX ");
		if(grade >= 0 && grade <= 29)
			System.out.println("Your grade is F ");
	}
}
