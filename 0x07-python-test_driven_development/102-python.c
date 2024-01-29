#include <Python.h>
#include <stdio.h>


void print_python_string(PyObject *p)
{
    /**
     * This function prints a Python string object in C
     * Args:
     * 	   p: a pointer to a PyObject
     * Format:
     *     [length] [type] [content]
     * Example:
     * 	   >>> s = "Hello"
     * 	   >>> print_python_string(s)
     * 	   5 str Hello
     * If p is not a valid string, print an error message
     */
    /* check if p is a valid string object*/
    if (!PyUnicode_Check(p))
    {
	    fprintf(stderr, "Invalid String Object\n");
	    return;
    }
    /* get the length, type and content of the string*/
    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    const char *type = NULL;
    const char *content = NULL;
    if (PyUnicode_IS_COMPACT_ASCII(p))
    {
        type = "str";
        content = PyUnicode_AsUTF8(p);
    }
    else
    {
        type = "str is not ascii";
        content = PyUnicode_AsUTF8(p);
    }
    /* print the string*/
    printf("%zd %s %s\n", length, type, content);
}
