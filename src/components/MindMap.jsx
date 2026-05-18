import { useState } from 'react';

function TreeNode({ node, level = 0 }) {
  const [open, setOpen] = useState(level < 2);
  const hasChildren = node.children && node.children.length > 0;

  return (
    <div className="mind-node" style={{ paddingLeft: level * 14 }}>
      <div className="mind-node-row" onClick={() => setOpen(!open)}>
        {hasChildren ? (
          <span className={`mind-arrow ${open ? 'open' : ''}`}>▶</span>
        ) : (
          <span className="mind-dot">·</span>
        )}
        {node.icon && <span className="mind-icon">{node.icon}</span>}
        <span className={`mind-name ${!hasChildren ? 'leaf' : ''}`}>{node.name}</span>
      </div>
      {open && hasChildren && (
        <div className="mind-children">
          {node.children.map((child, i) => (
            <TreeNode key={i} node={child} level={level + 1} />
          ))}
        </div>
      )}
    </div>
  );
}

export default function MindMap({ data }) {
  if (!data || !data.root) return null;
  return (
    <div className="mindmap-block">
      <div className="mindmap-title">{data.title}</div>
      <TreeNode node={data.root} level={0} />
    </div>
  );
}
