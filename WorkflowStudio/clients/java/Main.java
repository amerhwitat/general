package com.amerhwitat.chimeraworkflow;
import java.net.*;import java.io.*;
public final class Main { public static void main(String[] a)throws Exception{var s=new ServerSocket(8080);System.out.println("Chimera WorkFlow Java client/service ready on 8080");try(var x=s.accept()){x.getOutputStream().write("HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: 15\r\n\r\n{\"status\":\"ok\"}".getBytes());}} }
