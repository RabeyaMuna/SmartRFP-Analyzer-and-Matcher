import React from 'react';
import '../styles/table.css'; // Import the CSS file

function TableRow({ data }) {
  return (
    <tr className="row">
      <td className="cell key">{data.key}</td>
      <td className="cell value">{data.value}</td>
    </tr>
  );
}

export default TableRow;
