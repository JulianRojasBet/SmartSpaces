import { ReactNode } from "react";

type ModalProps = {
  id: string;
  children: ReactNode
};

export function Modal({ id, children }: ModalProps) {
  return (
    <>
      <div className="modal" id={id}>
        <div className="modal-box max-w-5xl">
          {children}
        </div>
      </div>
    </>
  );
}
