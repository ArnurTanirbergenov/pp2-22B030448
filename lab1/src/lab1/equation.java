package lab1;

import java.util.Scanner;

public class equation {
	public static void main(String args[]) {
		Scanner input = new Scanner(System.in);
		
		int a;
		int b;
		int c;
		double d;
		double root1;
		double root2;
		
		System.out.println("Enter a: ");
		a = input.nextInt();
		
		System.out.println("Enter b: ");
		b = input.nextInt();
		
		System.out.println("Enter c: ");
		c = input.nextInt();
		
		d = (int) Math.pow(b, 2) - 4 * a * c;
		
		if(d < 0)
			System.out.println("Error D is less than 0 ");
		else if(d == 0) {
			root1 = -b / (2 * a);
			root2 = root1;
			System.out.println("Your roots are " + root1 + ' ' + root2);
		}
		else {
			root1 = (-b + Math.sqrt(d))/ (2 * a);
			root2 = (-b - Math.sqrt(d))/ (2 * a);
			
			System.out.println("Your roots are " + root1 + ' ' + root2);
		}
	}
}
