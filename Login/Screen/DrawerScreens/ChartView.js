import BubbleChart from 'rn-bubble-chart';

function ChartView({ navigation }) {

  const data = [
    { name: "King Douchebag", color: "yellow", value: 90 },
    { name: "Princess Kenny", color: "pink", value: 60 },
    { name: "Heidi Turner", color: "red", value: 30 },
    { name: "Eric Cartman", color: "purple", value: 80 },
    { name: "Bart", color: "green", value: 40 }
  ]
  
    return(
      <BubbleChart
        width={400}
        height={300}
        data={data}
      />
    )
  }

  export default ChartView;