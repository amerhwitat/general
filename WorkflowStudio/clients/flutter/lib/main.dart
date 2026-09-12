import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter_tts/flutter_tts.dart';
void main()=>runApp(const WorkFlowApp());
class WorkFlowApp extends StatelessWidget{const WorkFlowApp({super.key});@override Widget build(BuildContext c)=>MaterialApp(title:'Chimera WorkFlow Studio',home:Scaffold(appBar:AppBar(title:const Text('Projects')),body:const Center(child:Text('Agile • DevOps • ITIL 4 • AI'))));}
class VoiceService{final FlutterTts tts=FlutterTts();Future<void>speak(String text,{String language='en-US'})async{await tts.setLanguage(language);await tts.speak(text);}}
Map<String,dynamic> decodeProject(String value)=>jsonDecode(value) as Map<String,dynamic>;
