import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3003;

// Servir archivos estáticos desde la carpeta infomesas2
const staticPath = '/home/waltermas/infomesas2';
app.use(express.static(staticPath));

// Ruta principal - sirve index.html
app.get('/', (req, res) => {
  res.sendFile(path.join(staticPath, 'index.html'));
});

// Iniciar servidor
app.listen(PORT, () => {
  console.log(`🚀 Servidor corriendo en http://localhost:${PORT}`);
  console.log(`📁 Sirviendo archivos desde: ${staticPath}`);
  console.log(`\n💡 Abrí tu navegador en: http://localhost:${PORT}`);
});

// Manejo de errores
app.use((err, req, res, next) => {
  console.error('❌ Error:', err.message);
  res.status(500).send('Error en el servidor');
});
