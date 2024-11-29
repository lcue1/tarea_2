package com.example.appguees

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {
    //Attributes
    lateinit var attemptsNumber: TextView
    lateinit var hints:TextView
    var nAttemmpts=3
    lateinit var entrada: EditText
    lateinit var btn_calcular: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
        //Init attributes
        attemptsNumber=findViewById(R.id.attemptsNumber)
        attemptsNumber.text="Numero de intentos${nAttemmpts.toString()}"
        hints=findViewById(R.id.hints)
        entrada=findViewById(R.id.ingreso)
        btn_calcular=findViewById(R.id.btn_calcular)
        btn_calcular.setOnClickListener {//Event listener
            val numberEdit=entrada.text.toString().toInt()// get number enter
            guesNumber(1,)//Function guess number

        }
    }
    val guesNumber= { numberEdit: Int ->
        val random = (0..9).random()//Generate random number


        if (random == numberEdit) {
            hints.text = "Win!"
            btn_calcular.isEnabled = false
        } else if (nAttemmpts == 1){
            hints.text = "Game Over!"
            btn_calcular.isEnabled = false

        }else if(numberEdit>random){
            hints.text="Too gratter!"
            nAttemmpts-=1
            attemptsNumber.text="Numero de intentos${nAttemmpts.toString()}"
        }else{
            hints.text="Too less!"
            nAttemmpts-=1
            attemptsNumber.text="Numero de intentos${nAttemmpts.toString()}"
        }

    }

}