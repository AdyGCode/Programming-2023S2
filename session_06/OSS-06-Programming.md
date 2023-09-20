[[OSS-05-Programming]] [[OSS-07-Programming]]
## Communications

- MS Teams
- eMail (online@screencraft.net.au)


## Useful Links
https://diigo.com/profile/ady_gould

## C# (Something Java Programmers cannot do)


```C#
int[] myArray;
void function abc( int[] theArray){}

abc(myArray);
```

[Passing arrays as arguments - C# Programming Guide | Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/passing-arrays-as-arguments)
```C#
using System;

class ArrayExample
{
	int[] intArr;

    static void DisplayArray(string[] arr) => Console.WriteLine(string.Join(" ", arr));

    static void DisplayArrayLonger(string[] arr) {
	    Console.WriteLine( string.Join(" ", arr) );
    }
    
    // Change the array by reversing its elements.
    static void ChangeArray(string[] arr) => Array.Reverse(arr);

    static void ChangeArrayElements(string[] arr)
    {
        // Change the value of the first three array elements.
        arr[0] = "Mon";
        arr[1] = "Wed";
        arr[2] = "Fri";
    }

    static void Main()
    {
        // Declare and initialize an array.
        string[] weekDays = { 
            "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" 
        };
        // Display the array elements.
        DisplayArray(weekDays);
        Console.WriteLine();

        // Reverse the array.
        ChangeArray(weekDays);
        // Display the array again to verify that it stays reversed.
        Console.WriteLine("Array weekDays after the call to ChangeArray:");
        DisplayArray(weekDays);
        Console.WriteLine();

        // Assign new values to individual array elements.
        ChangeArrayElements(weekDays);
        // Display the array again to verify that it has changed.
        Console.WriteLine("Array weekDays after the call to ChangeArrayElements:");
        DisplayArray(weekDays);
    }
}
// The example displays the following output:
//         Sun Mon Tue Wed Thu Fri Sat
//
//        Array weekDays after the call to ChangeArray:
//        Sat Fri Thu Wed Tue Mon Sun
//
//        Array weekDays after the call to ChangeArrayElements:
//        Mon Wed Fri Wed Tue Mon Sun
```
## Python Issues?
- What are you struggling to understand?


 