# Dice roll simulation app

library(shiny)

dice_rolls <- function(n_rolls, dice = 1:6){
  rolls_vect <- vector()
  for(roll in 1:n_rolls){
    num <- sample(dice, 1)
    if(num == 6){
      while(num == 6){
        num <- sample(dice, 1)
      }
    }
    rolls_vect[roll] <- num
  }
  rolls_vect
}

# Define UI
ui <- fluidPage(
  titlePanel("Dice rolls"),
  
  sidebarLayout(
    sidebarPanel(
      h3("A dice is rolled the number of times entered into the box. Any 6's are rolled again."), 
      textInput(
        inputId = "number_of_rolls",
        label = "Please enter a number:",
        placeholder = "Please enter a number", 
        value = "0"
      )
    ),
    
    mainPanel(
      h3("Outputs"),
      verbatimTextOutput("number_of_rolls_output"),
      verbatimTextOutput("sum_of_rolls_output"),
      plotOutput("plot_output")
    )
  )
)

# Define server logic
server <- function(input, output, session) {
  
  dice_rolls_result <- reactive({
    dice_rolls(input$number_of_rolls) 
  })
  
  # Number of rolls output
  output$number_of_rolls_output <- renderText({
    if (input$number_of_rolls == "") {
      "Please enter a number"
    } else {
      paste("You entered:", input$number_of_rolls)
    }
  })
  
  output$sum_of_rolls_output <- renderText({
    sum(dice_rolls_result())
  })
  
  # Plot output
  output$plot_output <- renderPlot({
    hist(dice_rolls_result())
  })
  
}

# Run the application
shinyApp(ui = ui, server = server)





