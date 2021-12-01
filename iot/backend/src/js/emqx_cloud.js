const options = {
    clean: true, 
    connectTimeout: 4000, 
    clientId: "emqx test",
    username: "",
    password: "",
}
const connect_mqtt = "wss://broker.emqx.io:8084/mqtt";
const cliente_mqtt = mqtt.connect(connect_mqtt,options)
cliente_mqtt.on("connect",() => {
    cliente_mqtt.subscribe("dashboard/#");
    console.log("connect succefully at port 1883");
});
cliente_mqtt.on("reconnect", (error) => {
    console.log("reconnecting: ", error)
})
cliente_mqtt.on("error",(error) => {
    console.log("Connection failed: ", error)
})
cliente_mqtt.on("message",(topic,message) => {
    console.log("receive message： ",topic,message.toString())
})
cliente_mqtt.publish("dashboard/bomba/estado","active")