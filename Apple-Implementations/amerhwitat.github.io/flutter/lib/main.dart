import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

void main() => runApp(const ApplePortfolioApp());

class ApplePortfolioApp extends StatelessWidget {
  const ApplePortfolioApp({super.key});
  static const native = MethodChannel('amerhwitat.apple/native');
  @override Widget build(BuildContext context) => MaterialApp(
    debugShowCheckedModeBanner: false,
    theme: ThemeData(useMaterial3: true, brightness: Brightness.light),
    darkTheme: ThemeData(useMaterial3: true, brightness: Brightness.dark),
    home: const Scaffold(body: Center(child: Text('Chimera Apple Application'))),
  );
}
