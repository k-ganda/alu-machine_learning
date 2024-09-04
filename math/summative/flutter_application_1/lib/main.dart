import 'dart:convert';
import 'package:intl/intl.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          centerTitle: true,
          backgroundColor: Colors.pink,
          title: const Text(
            "Insurance cost Prediction App",
            style: TextStyle(
              fontSize: 20,
              fontWeight: FontWeight.bold,
              color: Colors.black,
            ),
          ),
        ),
        body: const SingleChildScrollView(
          child: PredictionForm(),
        ),
      ),
    );
  }
}

class PredictionForm extends StatefulWidget {
  const PredictionForm({super.key});
  @override
  _PredictionFormState createState() => _PredictionFormState();
}

class _PredictionFormState extends State<PredictionForm> {
  // Text editing controllers
  final TextEditingController ageController = TextEditingController();
  final TextEditingController sexController = TextEditingController();
  final TextEditingController bmiController = TextEditingController();
  final TextEditingController childrenController = TextEditingController();
  final TextEditingController smokerController = TextEditingController();
  final TextEditingController regionController = TextEditingController();
  String result = ''; // stores the Predicted insurance cost

  Future<void> predict() async {
    final String url =
        'https://price-prediction-model-4ns5.onrender.com/predict';
    final Map<String, dynamic> data = {
      'age': int.parse(ageController.text),
      'sex': int.parse(sexController.text),
      'bmi': double.parse(bmiController.text),
      'children': int.parse(childrenController.text),
      'smoker': int.parse(smokerController.text),
      'region': int.parse(regionController.text),
    };

    try {
      final response = await http.post(
        Uri.parse(url),
        headers: {'Content-Type': 'application/json'},
        body: json.encode(data),
      );

      if (response.statusCode == 200) {
        final responseData =
            json.decode(response.body); // converts JSON to dart object
        setState(() {
          double charges = responseData['predicted_charges'];
          final formatter = NumberFormat.currency(
              locale: 'en_US', symbol: '\$', decimalDigits: 2);
          result = 'Predicted Charges: ${formatter.format(charges)}';
        });
      } else {
        final responseData = json.decode(response.body);
        String errorMessage = responseData['detail'].map((error) {
          return '${error['loc'][1]}: ${error['msg']} (got ${error['input']})';
        }).join(', ');
        setState(() {
          result = 'Error: $errorMessage';
        });
      }
    } catch (e) {
      setState(() {
        result = 'Error: $e';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(16.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          const Column(
            children: <Widget>[
              Center(
                child: Text(
                  "GET A GLIMPSE OF YOUR INSURANCE FUTURE",
                  style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                    color: Colors.pink,
                  ),
                  textAlign: TextAlign.center,
                ),
              ),
              SizedBox(height: 20),
              Text(
                "Predict your cost Now!",
                style: TextStyle(
                  fontSize: 18,
                  color: Colors.black,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
          const SizedBox(height: 20),
          TextFormField(
            controller: ageController,
            decoration: const InputDecoration(
              labelText: 'Age',
              border: OutlineInputBorder(
                borderRadius: BorderRadius.all(Radius.circular(10.0)),
                borderSide: BorderSide(color: Colors.pink),
              ),
              hintText: 'Enter your age (18+)',
            ),
            keyboardType: TextInputType.number,
          ),
          const SizedBox(height: 20),
          TextFormField(
            controller: sexController,
            decoration: const InputDecoration(
              labelText: 'Sex',
              border: OutlineInputBorder(
                borderRadius: BorderRadius.all(Radius.circular(10.0)),
                borderSide: BorderSide(color: Colors.pink),
              ),
              hintText: 'Enter (0 for male, 1 for female)',
            ),
            keyboardType: TextInputType.number,
          ),
          const SizedBox(height: 20),
          TextFormField(
            controller: bmiController,
            decoration: const InputDecoration(
              labelText: 'BMI',
              border: OutlineInputBorder(
                borderRadius: BorderRadius.all(Radius.circular(10.0)),
                borderSide: BorderSide(color: Colors.pink),
              ),
              hintText: 'Enter your Body Mass Index',
            ),
            keyboardType: TextInputType.number,
          ),
          const SizedBox(height: 20),
          TextFormField(
            controller: childrenController,
            decoration: const InputDecoration(
              labelText: 'Children',
              border: OutlineInputBorder(
                borderRadius: BorderRadius.all(Radius.circular(10.0)),
                borderSide: BorderSide(color: Colors.pink),
              ),
              hintText: 'Enter the number of children',
            ),
            keyboardType: TextInputType.number,
          ),
          const SizedBox(height: 20),
          TextFormField(
            controller: smokerController,
            decoration: const InputDecoration(
              labelText: 'Smoker',
              border: OutlineInputBorder(
                borderRadius: BorderRadius.all(Radius.circular(10.0)),
                borderSide: BorderSide(color: Colors.pink),
              ),
              hintText: 'Enter (0 for no, 1 for yes)',
            ),
            keyboardType: TextInputType.number,
          ),
          const SizedBox(height: 20),
          TextFormField(
            controller: regionController,
            decoration: const InputDecoration(
              labelText: 'Region',
              border: OutlineInputBorder(
                borderRadius: BorderRadius.all(Radius.circular(10.0)),
                borderSide: BorderSide(color: Colors.pink),
              ),
              hintText: 'Enter (0-NW, 1-NE, 2-SE, 3-SW)',
            ),
            keyboardType: TextInputType.number,
          ),
          const SizedBox(height: 20),
          Center(
            child: SizedBox(
              width: 200,
              child: ElevatedButton(
                onPressed: () async {
                  if (ageController.text.isEmpty ||
                      sexController.text.isEmpty ||
                      bmiController.text.isEmpty ||
                      childrenController.text.isEmpty ||
                      smokerController.text.isEmpty ||
                      regionController.text.isEmpty) {
                    setState(() {
                      result = 'Please fill in all fields';
                    });
                    return;
                  }
                  await predict();
                },
                style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all(Colors.pink),
                  shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                    RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10.0),
                    ),
                  ),
                ),
                child: const Text(
                  'Predict',
                  style: TextStyle(
                    color: Colors.white,
                  ),
                ),
              ),
            ),
          ),
          const SizedBox(height: 20),
          Center(
            child: Text(
              result,
              style: const TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.bold,
                color: Colors.black,
              ),
              textAlign: TextAlign.center,
            ),
          ),
        ],
      ),
    );
  }
}
