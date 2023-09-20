package lab1;

import java.util.Scanner;

public class square {
	public static void main(String args[]) {
		
		Scanner input = new Scanner(System.in);
		
		int side;
		int area;
		int perimetr;
		double diagonal;
		
		System.out.println("side: ");
		side = input.nextInt();
		
		area = side * side;
		perimetr = side * 4;
		diagonal = Math.sqrt(2) * side;
		
		System.out.println("Area: " + area);
		System.out.println("Perimetr: " + perimetr);
		System.out.println("Diagonal: " + diagonal);
	}
}
