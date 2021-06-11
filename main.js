async function send_image() {
    const photo = document.getElementById("img-file").files[0]        
    let formData = new FormData() 
    formData.append("image_file", photo)

    const res = await fetch("INSERT URL", {
        method: "POST",
        body: formData,
    })

    const data = await res.blob();
    const imgURL = URL.createObjectURL(data);
    document.querySelector("img").src = imgURL;
} 