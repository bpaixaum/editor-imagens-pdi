import PySimpleGUI as sg
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from io import BytesIO

def convert_to_bytes(img, resize=True, maxsize=(600, 400)):
    if resize:
        h, w = img.shape[:2]
        scale = min(maxsize[0] / w, maxsize[1] / h)
        if scale < 1:
            img = cv2.resize(img, (int(w * scale), int(h * scale)))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(img)
    with BytesIO() as output:
        im_pil.save(output, format="PNG")
        data = output.getvalue()
    return data

layout = [
    [sg.Text("Editor de Imagens - PDI")],
    [sg.Image(filename="", key="-IMAGE-")],
    [sg.Button("Carregar Imagem"), sg.Button("Salvar"), sg.Button("Histograma"), sg.Button("Alargamento de Contraste"),
     sg.Button("Equalização de Histograma"), sg.Button("Filtro: Média"), sg.Button("Filtro: Mediana"),
     sg.Button("Filtro: Gaussiano"), sg.Button("Filtro: Máximo"), sg.Button("Filtro: Mínimo"),
     sg.Button("Filtro: Laplaciano"), sg.Button("Filtro: Sobel"), sg.Button("Filtro: Prewitt"),
     sg.Button("Filtro: Roberts"), sg.Button("Espectro de Fourier"), sg.Button("Dilatação"), sg.Button("Erosão"),
     sg.Button("Segmentação (Otsu)"), sg.Button("Descritor de Cor"), sg.Button("Sair")]
]

window = sg.Window("Editor de Imagens", layout, resizable=True, finalize=True)

image = None
filename = None

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "Sair"):
        break

    elif event == "Carregar Imagem":
        filepath = sg.popup_get_file("Escolha uma imagem", file_types=(("Imagens", "*.png;*.jpg;*.jpeg"),))
        if filepath:
            image = cv2.imread(filepath)
            filename = filepath
            img_bytes = convert_to_bytes(image, resize=True)
            window["-IMAGE-"].update(data=img_bytes)

    elif event == "Salvar":
        if image is not None:
            save_path = sg.popup_get_file("Salvar imagem como", save_as=True, default_extension=".png", file_types=(("PNG (*.png)", "*.png"),))
            if save_path:
                cv2.imwrite(save_path, image)
                sg.popup("Imagem salva com sucesso!")

    elif event == "Histograma":
        if image is not None:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            plt.figure("Histograma")
            plt.hist(gray.ravel(), 256, [0, 256])
            plt.title("Histograma da Imagem")
            plt.xlabel("Intensidade")
            plt.ylabel("Frequência")
            plt.show()

    elif event == "Alargamento de Contraste":
        if image is not None:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            norm_img = cv2.normalize(gray, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
            image = cv2.cvtColor(norm_img, cv2.COLOR_GRAY2BGR)
            img_bytes = convert_to_bytes(image, resize=True)
            window["-IMAGE-"].update(data=img_bytes)
            sg.popup("Contraste alargado com sucesso!")

    elif event == "Equalização de Histograma":
        if image is not None:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            equalized = cv2.equalizeHist(gray)
            image = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)
            img_bytes = convert_to_bytes(image, resize=True)
            window["-IMAGE-"].update(data=img_bytes)
            sg.popup("Equalização de histograma aplicada com sucesso!")

    elif event == "Filtro: Média":
        if image is not None:
            image = cv2.blur(image, (5, 5))
            img_bytes = convert_to_bytes(image, resize=True)
            window["-IMAGE-"].update(data=img_bytes)
            sg.popup("Filtro de Média aplicado!")

    elif event == "Filtro: Mediana":
        if image is not None:
            image = cv2.medianBlur(image, 5)
            img_bytes = convert_to_bytes(image, resize=True)
            window["-IMAGE-"].update(data=img_bytes)
            sg.popup("Filtro de Mediana aplicado!")

    elif event == "Filtro: Gaussiano":
        if image is not None:
            image = cv2.GaussianBlur(image, (5, 5), 0)
            img_bytes = convert_to_bytes(image, resize=True)
            window["-IMAGE-"].update(data=img_bytes)
            sg.popup("Filtro Gaussiano aplicado!")

    elif event == "Filtro: Máximo":
        if image is not None:
            kernel = np.ones((5, 5), np.uint8)
            image = cv2.dilate(image, kernel)
            img_bytes = convert_to_bytes(image, resize=True)
            window["-IMAGE-"].update(data=img_bytes)
            sg.popup("Filtro Máximo (Dilatação) aplicado!")

    elif event == "Filtro: Mínimo":
        if image is not None:
            kernel = np.ones((5, 5), np.uint8)
            image = cv2.erode(image, kernel)
            img_bytes = convert_to_bytes(image, resize=True)
            window["-IMAGE-"].update(data=img_bytes)
            sg.popup("Filtro Mínimo (Erosão) aplicado!")

    elif event == "Filtro: Laplaciano":
        if image is not None:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            lap = cv2.Laplacian(gray, cv2.CV_64F)
            lap = cv2.convertScaleAbs(lap)
            image = cv2.cvtColor(lap, cv2.COLOR_GRAY2BGR)
            img_bytes = convert_to_bytes(image, resize=True)
            window["-IMAGE-"].update(data=img_bytes)
            sg.popup("Filtro Laplaciano aplicado!")

    elif event == "Filtro: Sobel":
        if image is not None:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
            sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
            sobel = cv2.magnitude(sobelx, sobely)
            sobel = cv2.convertScaleAbs(sobel)
            image = cv2.cvtColor(sobel, cv2.COLOR_GRAY2BGR)
            img_bytes = convert_to_bytes(image, resize=True)
            window["-IMAGE-"].update(data=img_bytes)
            sg.popup("Filtro Sobel aplicado!")

    elif event == "Filtro: Prewitt":
        if image is not None:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
            kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
            prewittx = cv2.filter2D(gray, -1, kernelx)
            prewitty = cv2.filter2D(gray, -1, kernely)
            prewitt = cv2.magnitude(prewittx.astype(np.float32), prewitty.astype(np.float32))
            prewitt = cv2.convertScaleAbs(prewitt)
            image = cv2.cvtColor(prewitt, cv2.COLOR_GRAY2BGR)
            img_bytes = convert_to_bytes(image, resize=True)
            window["-IMAGE-"].update(data=img_bytes)
            sg.popup("Filtro Prewitt aplicado!")

    elif event == "Filtro: Roberts":
        if image is not None:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            kernelx = np.array([[1, 0], [0, -1]])
            kernely = np.array([[0, 1], [-1, 0]])
            robertsx = cv2.filter2D(gray, -1, kernelx)
            robertsy = cv2.filter2D(gray, -1, kernely)
            roberts = cv2.magnitude(robertsx.astype(np.float32), robertsy.astype(np.float32))
            roberts = cv2.convertScaleAbs(roberts)
            image = cv2.cvtColor(roberts, cv2.COLOR_GRAY2BGR)
            img_bytes = convert_to_bytes(image, resize=True)
            window["-IMAGE-"].update(data=img_bytes)
            sg.popup("Filtro Roberts aplicado!")

    elif event == "Espectro de Fourier":
        if image is not None:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            f = np.fft.fft2(gray)
            fshift = np.fft.fftshift(f)
            magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)
            plt.figure("Espectro de Fourier")
            plt.imshow(magnitude_spectrum, cmap='gray')
            plt.title("Espectro de Fourier")
            plt.axis("off")
            plt.show()

    elif event == "Dilatação":
        if image is not None:
            kernel = np.ones((5, 5), np.uint8)
            image = cv2.dilate(image, kernel, iterations=1)
            img_bytes = convert_to_bytes(image, resize=True)
            window["-IMAGE-"].update(data=img_bytes)
            sg.popup("Dilatação aplicada!")

    elif event == "Erosão":
        if image is not None:
            kernel = np.ones((5, 5), np.uint8)
            image = cv2.erode(image, kernel, iterations=1)
            img_bytes = convert_to_bytes(image, resize=True)
            window["-IMAGE-"].update(data=img_bytes)
            sg.popup("Erosão aplicada!")

    elif event == "Segmentação (Otsu)":
        if image is not None:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            image = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
            img_bytes = convert_to_bytes(image, resize=True)
            window["-IMAGE-"].update(data=img_bytes)
            sg.popup("Segmentação com Otsu aplicada!")

    elif event == "Descritor de Cor":
        if image is not None:
            chans = cv2.split(image)
            colors = ("b", "g", "r")
            plt.figure("Descritor de Cor - Histograma RGB")
            for chan, color in zip(chans, colors):
                hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
                hist = hist / hist.sum()
                plt.plot(hist, color=color)
                plt.xlim([0, 256])
            plt.title("Histograma Normalizado por Canal de Cor")
            plt.xlabel("Intensidade")
            plt.ylabel("Frequência Normalizada")
            plt.show()

window.close()
