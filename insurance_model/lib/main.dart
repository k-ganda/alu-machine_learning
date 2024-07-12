import 'package:flutter/material.dart';

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
          body: SingleChildScrollView(
            child: PredictionForm(),
          )),
    );
  }
}

class PredictionForm extends StatefulWidget {
  @override
  _PredictionFormState createState() => _PredictionFormState();
}

class _PredictionFormState extends State<PredictionForm> {
  final TextEditingController ageController = TextEditingController();
  final TextEditingController sexController = TextEditingController();
  final TextEditingController bmiController = TextEditingController();
  final TextEditingController childrenController = TextEditingController();
  final TextEditingController smokerController = TextEditingController();
  final TextEditingController regionController = TextEditingController();

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
            decoration: InputDecoration(
              labelText: 'Age',
              border: OutlineInputBorder(
                borderRadius: BorderRadius.all(Radius.circular(10.0)),
                borderSide: BorderSide(color: Colors.pink),
              ),
              hintText: 'Enter your age(18+)',
            ),
            keyboardType: TextInputType.number,
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Please enter your age';
              }
              return null;
            },
          ),
          const SizedBox(height: 20),
          TextFormField(
            controller: ageController,
            decoration: InputDecoration(
              labelText: 'Sex',
              border: OutlineInputBorder(
                borderRadius: BorderRadius.all(Radius.circular(10.0)),
                borderSide: BorderSide(color: Colors.pink),
              ),
              hintText: 'Enter (0 for male, 1 for female)',
            ),
            keyboardType: TextInputType.number,
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Please enter your sex';
              }
              return null;
            },
          ),
          const SizedBox(height: 20),
          TextFormField(
            controller: ageController,
            decoration: InputDecoration(
              labelText: 'BMI',
              border: OutlineInputBorder(
                borderRadius: BorderRadius.all(Radius.circular(10.0)),
                borderSide: BorderSide(color: Colors.pink),
              ),
              hintText: 'Enter your Body Mass Index',
            ),
            keyboardType: TextInputType.number,
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Please enter your BMI';
              }
              return null;
            },
          ),
          const SizedBox(height: 20),
          TextFormField(
            controller: ageController,
            decoration: InputDecoration(
              labelText: 'Children',
              border: OutlineInputBorder(
                borderRadius: BorderRadius.all(Radius.circular(10.0)),
                borderSide: BorderSide(color: Colors.pink),
              ),
              hintText: 'Enter the no of children ',
            ),
            keyboardType: TextInputType.number,
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Please enter no of children';
              }
              return null;
            },
          ),
          const SizedBox(height: 20),
          TextFormField(
            controller: ageController,
            decoration: InputDecoration(
              labelText: 'Smoker',
              border: OutlineInputBorder(
                borderRadius: BorderRadius.all(Radius.circular(10.0)),
                borderSide: BorderSide(color: Colors.pink),
              ),
              hintText: 'Enter(0 for no, 1 for yes)',
            ),
            keyboardType: TextInputType.number,
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Please enter your smoking status';
              }
              return null;
            },
          ),
          const SizedBox(height: 20),
          TextFormField(
            controller: ageController,
            decoration: InputDecoration(
              labelText: 'Region',
              border: OutlineInputBorder(
                borderRadius: BorderRadius.all(Radius.circular(10.0)),
                borderSide: BorderSide(color: Colors.pink),
              ),
              hintText: 'Enter (0-NW, 1-NE, 2-SE, 3-SW)',
            ),
            keyboardType: TextInputType.number,
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Please enter your region';
              }
              return null;
            },
          ),
          const SizedBox(height: 20),
          Center(
            child: SizedBox(
              width: 200, // Set your desired width here
              child: ElevatedButton(
                onPressed: () {
                  // Add your prediction logic here
                },
                style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all(Colors.pink),
                  shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                    RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10.0),
                    ),
                  ),
                ),
                child: Text(
                  'Predict',
                  style: TextStyle(
                    color: Colors.white,
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
